from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from actions.models import Action
from tasks.models import Task
from actions.forms import ActionCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required
def actions_list_view(request, *args, **kwargs):
    context = {
        "actions": Action.objects.all(),
        "page_title": "Open actions",
        "user":request.user,
    }
    
    return render(request, 'actions_list.html', context) 

@login_required
def action_detail_view(request, id):
    obj = get_object_or_404(Action, id=id)
    context = {
        "action": obj,
    }
    return render(request, 'action_detail.html', context)

@login_required
def action_update_view(request, id):
    obj = get_object_or_404(Action, id=id)
    form = ActionCreationForm(request.POST or None, instance=obj)
    if form.is_valid():
        previous_object = Action.objects.get(id=form.instance.id)
        form_obj = form.save()
        redirect_project = form_obj.task.project
        if previous_object.completed == False and form.instance.completed == True:
            form_obj.completed_at = datetime.datetime.now()
        elif previous_object.completed == True and form.instance.completed == False:
            form_obj.completed_at = None
        form_obj.updated_at = datetime.datetime.now()
        form_obj.save()
        form = ActionCreationForm()
        return redirect(redirect_project.get_absolute_url())
    context = {
        "form" : form
    }
    return render(request, 'action_create.html', context)

@login_required
def action_delete_view(request, id):
    obj = get_object_or_404(Action, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        "action": obj,
    }
    return render(request, 'action_delete.html', context)

@login_required
def action_complete_view(request, id):
    obj = get_object_or_404(Action, id=id)
    obj.completed_at = datetime.datetime.now()
    obj.completed = True
    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def action_complete_and_next_view(request, id):
    if request.POST:
        form = ActionCreationForm(request.POST)
    else:
        obj = get_object_or_404(Action, id=id)
        obj.completed_at = datetime.datetime.now()
        obj.completed = True
        obj.save()
        initial_data = {
            'owner': obj.owner,
            'duedate': datetime.datetime.now().date(),
            'assignee': obj.assignee,
            'previous_url' : request.META.get('HTTP_REFERER'),
            'task': obj.task,
        }
        form = ActionCreationForm(initial=initial_data)
        form.fields['task'].queryset = Task.objects.filter(project_id=obj.task.project.id)
    if form.is_valid():
        previous_ulr = form.cleaned_data['previous_url']
        form.save()
        return redirect(previous_ulr)
    context = {
        "form" : form,
    }
    return render(request, 'action_create.html', context)

@login_required
def action_create_view(request, taskid=None, projectid=None):
    if request.POST:
        form = ActionCreationForm(request.POST)
    else:
        initial_data = {
            'owner': request.user,
            'duedate': datetime.datetime.now().date(),
            'assignee': request.user,
            'previous_url' : request.META.get('HTTP_REFERER')
        }
        if taskid and projectid:
            initial_data['task'] = taskid 
        form = ActionCreationForm(initial=initial_data)
        if projectid:
            form.fields['task'].queryset = Task.objects.filter(project_id=projectid)
    if form.is_valid():
        previous_ulr = form.cleaned_data['previous_url']
        form.save()
        return redirect(previous_ulr)
    context = {
        "form" : form,
    }
    return render(request, 'action_create.html', context)