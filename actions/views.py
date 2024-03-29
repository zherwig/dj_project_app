from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from actions.models import Action
from dashboards import applogic
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
    initial_data = {
        'previous_url' : request.META.get('HTTP_REFERER'),
    }
    request_data = None
    if request.POST:
        request_data = request.POST.copy()
        request_data['task'] = str(Task.objects.filter(title=request.POST.get('task')).first().id)
    form = ActionCreationForm(request_data or None, instance=obj, initial=initial_data)   
    if form.is_valid():
        previous_url = form.cleaned_data['previous_url']
        previous_object = Action.objects.get(id=form.instance.id)
        form_obj = form.save()
        if previous_object.completed == False and form.instance.completed == True:
            form_obj.completed_at = datetime.datetime.now()
        elif previous_object.completed == True and form.instance.completed == False:
            form_obj.completed_at = None
        form_obj.updated_at = datetime.datetime.now()
        form_obj.save()
        return redirect(previous_url)
    context = {
        "form" : form
    }
    return render(request, 'action_create.html', context)

@login_required
def action_delete_view(request, id):
    obj = get_object_or_404(Action, id=id)
    if request.method == 'POST':
        previous_url = obj.task.get_absolute_url()
        obj.delete()
        return redirect(previous_url)
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
        request_data = request.POST.copy()
        request_data['task'] = str(Task.objects.filter(title=request.POST.get('task')).first().id)
        form = ActionCreationForm(request_data)
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
def action_create_view(request, taskid=None, projectid=None, assignee=None):
    if not assignee:
        assignee = request.user
    else:
        try:
            assignee = User.objects.get(username__contains=assignee.lower())
        except:
            assignee = request.user

    if request.POST:
        request_data = request.POST.copy()
        request_data['task'] = str(Task.objects.filter(title=request.POST.get('task')).first().id)
        form = ActionCreationForm(request_data)
    else:
        initial_data = {
            'owner': request.user,
            'duedate': datetime.datetime.now().date(),
            'assignee': assignee,
            'previous_url' : request.META.get('HTTP_REFERER')
        }
        if taskid and projectid:
            initial_data['task'] = taskid 
        form = ActionCreationForm(initial=initial_data)
        # if projectid:
        #     form.fields['task'].queryset = Task.objects.filter(project_id=projectid)
    if form.is_valid():
        previous_ulr = form.cleaned_data['previous_url']
        form.save()
        return redirect(previous_ulr)
    context = {
        "form" : form,
    }
    return render(request, 'action_create.html', context)

@login_required
def action_highlight_toggle_view(request, id):
    obj = get_object_or_404(Action, id=id)
    if obj.highlighted == True:
        obj.highlighted = False
    else:
        obj.highlighted = True
    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def action_mute_toggle_view(request, id):
    obj = get_object_or_404(Action, id=id)
    if obj.muted == True:
        obj.muted = False
    else:
        obj.muted = True
    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def action_delay_to_next_week(request, id):
    obj = get_object_or_404(Action, id=id)
    if obj.duedate.weekday() == 6:
        obj.duedate = obj.duedate + datetime.timedelta(days = 7)
    else:
        obj.duedate = (obj.duedate - datetime.timedelta(days=obj.duedate.weekday())) + datetime.timedelta(days = 6)
    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def action_delay_to_next_month(request, id):
    obj = get_object_or_404(Action, id=id)
    obj.duedate = (obj.duedate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def action_delay_by_a_day_view(request, id):
    obj = get_object_or_404(Action, id=id)
    action_result = applogic.move_action_to_tomorrow(obj.id)
    if action_result:
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse(f'Exception: {action_result}')