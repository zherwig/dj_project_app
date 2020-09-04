from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from tasks.models import Task
from tasks.forms import TaskCreationForm
from django.contrib.auth.models import User

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
    }
    return render(request, 'task_detail.html', context)

def task_update_view(request, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskCreationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
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
        return redirect("../")
    context = {
        "task": obj,
    }
    return render(request, 'task_delete.html', context)

def task_create_view(request):
    form = TaskCreationForm(request.POST or None) 
    if form.is_valid():
        form.save()
        form = TaskCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'task_create.html', context)