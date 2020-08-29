from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project
from projects.forms import ProjectCreationForm
from django.contrib.auth.models import User

# Project.objects.get(id=1)

# Create your views here.
def projects_list_view(request, *args, **kwargs):
    context = {
        "projects": Project.objects.all(),
        "user":request.user,
    }
    
    return render(request, 'projects_list.html', context) 

def project_detail_view(request, *args, **kwargs):
    context = {
        "project": Project.objects.get(id=1),
    }
    return render(request, 'project_detail.html', context)

def project_create_view(request):
    if request.method == 'POST':
        new_project = Project(
            title = request.POST.get('title'),
            detail = request.POST.get('detail'),
            closed = False if request.POST.get('closed') == 'on' else True,
            onHold = False if request.POST.get('onHold') == 'on' else True,
            priority = request.POST.get('priority'),
            placeInOrder = request.POST.get('placeInOrder'),
            duedate = request.POST.get('duedate'),
            owner = User.objects.get(id=request.POST.get('owner')),
            assignee = User.objects.get(id=request.POST.get('assignee')),
        )
        new_project.save()
    context = {}
    return render(request, 'project_create.html', context)