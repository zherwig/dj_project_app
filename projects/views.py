from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project

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
