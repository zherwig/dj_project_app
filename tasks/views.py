from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task
from actions.models import Action
from tasks.forms import TaskCreationForm
from django.contrib.auth.models import User
import datetime

# Create your views here.
def tasks_list_view(request, *args, **kwargs):
    context = {
        "tasks": Task.objects.all(),
        "page_title": "Open tasks",
        "user":request.user,
    }
    
    return render(request, 'tasks_list.html', context) 

def task_detail_view(request, id):
    obj = get_object_or_404(Task, id=id)
    context = {
        "task": obj,
        "completed_actions": Action.objects.filter(task_id=obj.id).filter(completed=True),
        "open_actions": Action.objects.filter(task_id=obj.id).filter(completed=False).order_by('duedate'),
    }
    return render(request, 'task_detail.html', context)

def task_update_view(request, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskCreationForm(request.POST or None, instance=obj)
    if form.is_valid():
        previous_object = Task.objects.get(id=form.instance.id)
        form_obj = form.save()
        if previous_object.completed == False and form.instance.completed == True:
            form_obj.completed_at = datetime.datetime.now()
        elif previous_object.completed == True and form.instance.completed == False:
            form_obj.completed_at = None
        form_obj.updated_at = datetime.datetime.now()
        form_obj.save()
        form = TaskCreationForm()
        return redirect("../")
    context = {
        "form" : form
    }
    return render(request, 'task_create.html', context)

def task_delete_view(request, id):
    obj = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        "task": obj,
    }
    return render(request, 'task_delete.html', context)

def task_create_view(request, projectid=None):
    if request.POST:
        form = TaskCreationForm(request.POST)
    elif projectid:
        initial_data = {
            'owner': request.user,
            'assignee': request.user,
            'duedate': datetime.datetime.now().date(),
            'project': projectid
        }
        form = TaskCreationForm(initial=initial_data)
    else:
        initial_data = {
            'owner': request.user,
            'duedate': datetime.datetime.now().date(),
            'assignee': request.user,
        }
        form = TaskCreationForm(initial=initial_data)
    if form.is_valid():
        form.save()
        form = TaskCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'task_create.html', context)