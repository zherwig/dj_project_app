from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project
from projects.forms import ProjectCreationForm, RawProjectCreationForm
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
    form = RawProjectCreationForm() 
    if request.method == 'POST':
        form = RawProjectCreationForm(request.POST)
        if form.is_valid():
            new_project = Project(**form.cleaned_data)
            new_project.save()
            form = RawProjectCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'project_create.html', context)