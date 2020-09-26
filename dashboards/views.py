from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dashboards import applogic as dashboard_applogic

# Create your views here.
@login_required
def dashboard_list_view(request, *args, **kwargs):
    dashboard_applogic.get_topics_with_projects_and_open_tasks()
    context = {
        "topics": dashboard_applogic.get_topics_with_projects_and_open_tasks(),
        "user":request.user,
    }
    
    return render(request, 'dashboard_list.html', context) 


