from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from dashboards import applogic as dashboard_applogic
import datetime

# Create your views here.
@login_required
def dashboard_list_view(request, *args, **kwargs):
    context = {
        "topics": dashboard_applogic.get_topics_with_projects_and_open_tasks(),
        "user":request.user,
    }
    
    return render(request, 'dashboard_list.html', context) 


@login_required
def dashboard_actions_view(request, *args, **kwargs):   
    context = {
        "task_batches": [
            {
                'name':'Overdue',
                'tasks': dashboard_applogic.get_actions_per_date_range(-900, -1)
            },
            {
                'name':'Today',
                'tasks': dashboard_applogic.get_actions_per_date_range(0, 0)
            },
            {
                'name':'Tomorrow',
                'tasks': dashboard_applogic.get_actions_per_date_range(1, 1)
            },
            {
                'name':'Rest of the week',
                'tasks': dashboard_applogic.get_actions_per_date_range(2, 7)
            },
            {
                'name':'Rest of the month',
                'tasks': dashboard_applogic.get_actions_per_date_range(8, 30)
            },
        ],
        "user":request.user,
    }
    
    return render(request, 'dashboard_todos.html', context) 

@login_required
def dashboard_actions_fix_overdues(request, *args, **kwargs):   
    overdue_actions = dashboard_applogic.get_actions_per_date_range(-900, -1)
    for overdue_action in overdue_actions:
        dashboard_applogic.move_action_to_today(overdue_action.id)
    return redirect("/todos")
