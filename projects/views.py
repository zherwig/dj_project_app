from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectCreationForm, RawProjectCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime

# Project.objects.get(id=1)

# Create your views here.
@login_required
def projects_list_view(request, *args, **kwargs):
    context = {
        "projects": Project.objects.filter(closed=False),
        "page_title": "Open projects",
        "user":request.user,
    }
    
    return render(request, 'projects_list.html', context) 

def closed_projects_list_view(request, *args, **kwargs):
    context = {
        "projects": Project.objects.filter(closed=True),
        "page_title": "Closed projects",
        "user":request.user,
    }
    
    return render(request, 'projects_list.html', context) 

def project_detail_view(request, id):
    obj = get_object_or_404(Project, id=id)
    context = {
        "project": obj,
        "completed_tasks": Task.objects.filter(project_id=obj.id).filter(completed=True),
        "open_tasks": Task.objects.filter(project_id=obj.id).filter(completed=False).order_by('duedate'),
    }
    return render(request, 'project_detail.html', context)

def project_update_view(request, id):
    obj = get_object_or_404(Project, id=id)
    form = ProjectCreationForm(request.POST or None, instance=obj)
    if form.is_valid():
        previous_object = Project.objects.get(id=form.instance.id)
        form_obj = form.save()
        if previous_object.closed == False and form.instance.closed == True:
            form_obj.completed_at = datetime.datetime.now()
        elif previous_object.closed == True and form.instance.closed == False:
            form_obj.completed_at = None
        form_obj.updated_at = datetime.datetime.now()
        form_obj.save()
        form = ProjectCreationForm()
        return redirect("../")
    context = {
        "form" : form
    }
    return render(request, 'project_create.html', context)

def project_delete_view(request, id):
    obj = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        "project": obj,
    }
    return render(request, 'project_delete.html', context)

def project_create_view(request, topicid=None):
    if request.POST:
        form = ProjectCreationForm(request.POST)
    elif topicid:
        initial_data = {
            'owner': request.user,
            'assignee': request.user,
            'duedate': datetime.datetime.now().date(),
            'topic': topicid
        }
        form = ProjectCreationForm(initial=initial_data)
    else:
        initial_data = {
            'owner': request.user,
            'duedate': datetime.datetime.now().date(),
            'assignee': request.user,
        }
        form = ProjectCreationForm(initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProjectCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'project_create.html', context)