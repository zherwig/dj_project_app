from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectCreationForm
from notes.forms import AddNoteForm
from notes.applogic import getRelatedNotes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from projects import applogic as project_applogic
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

@login_required
def closed_projects_list_view(request, *args, **kwargs):
    context = {
        "projects": Project.objects.filter(closed=True),
        "page_title": "Closed projects",
        "user":request.user,
    }
    
    return render(request, 'projects_list.html', context) 

@login_required
def project_detail_view(request, id):
    obj = get_object_or_404(Project, id=id)
    notes = getRelatedNotes("project", id)
    form = AddNoteForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save()
        form_obj.project = obj
        form_obj.note_created_by = request.user
        form_obj.note_updated_by = request.user
        form_obj.updated_at = datetime.datetime.now()
        form_obj.created_at = datetime.datetime.now()
        form_obj.save()
        form = AddNoteForm()
    context = {
        "notes": notes,
        "form": form,
        "project": obj,
        "completed_tasks": Task.objects.filter(project_id=obj.id).filter(completed=True),
        "open_tasks": project_applogic.get_tasks_and_open_and_closed_actions(obj.id),
    }
    return render(request, 'project_detail.html', context)

@login_required
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
        return redirect('projects:project_detail_view', id = obj.id)
    context = {
        "form" : form,
        "title": f"Update Project: {obj.title}"
    }
    return render(request, 'project_create.html', context)

@login_required
def project_complete_view(request, id):
    obj = get_object_or_404(Project, id=id)
    open_tasks = Task.objects.filter(project_id = id).filter(completed = False)
    if open_tasks:
        return redirect('projects:project_detail_view', id = obj.id)
    obj.closed = True
    obj.completed_at = datetime.datetime.now()
    obj.save()
    return redirect(reverse('dashboards:home'))
    
@login_required
def project_delete_view(request, id):
    obj = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        "project": obj,
    }
    return render(request, 'project_delete.html', context)

@login_required
def project_create_view(request, topicid=None):
    if request.POST:
        form = ProjectCreationForm(request.POST)
    elif topicid:
        initial_data = {
            'owner': request.user,
            'assignee': request.user,
            'topic': topicid
        }
        form = ProjectCreationForm(initial=initial_data)
    else:
        initial_data = {
            'owner': request.user,
            'assignee': request.user,
        }
        form = ProjectCreationForm(initial=initial_data)
    if form.is_valid():
        form.save()
        return redirect('projects:project_detail_view', id = form.instance.id)
    context = {
        "form" : form,
        "title": "Create Project"

    }
    return render(request, 'project_create.html', context)