from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectCreationForm, RawProjectCreationForm
from django.contrib.auth.models import User
import datetime

# Project.objects.get(id=1)

# Create your views here.
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
        form_obj = form.save()
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
        return redirect("../")
    context = {
        "project": obj,
    }
    return render(request, 'project_delete.html', context)

def project_create_view(request):
    form = ProjectCreationForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form = ProjectCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'project_create.html', context)