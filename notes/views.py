from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Note
from tasks.models import Task
from actions.models import Action
from projects.models import Project
from notes.forms import NoteCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required
def notes_list_view(request, *args, **kwargs):
    context = {
        "notes": Note.objects.all(),
        "page_title": "Open notes",
        "user":request.user,
    }
    
    return render(request, 'notes_list.html', context) 

@login_required
def note_detail_view(request, id):
    obj = get_object_or_404(Note, id=id)
    context = {
        "note": obj,
    }
    return render(request, 'note_detail.html', context)

@login_required
def note_update_view(request, id):
    obj = get_object_or_404(Note, id=id)
    form = NoteCreationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form_obj = form.save()
        form_obj.updated_at = datetime.datetime.now()
        form_obj.save()
        form = NoteCreationForm()
        return redirect("../")
    context = {
        "form" : form
    }
    return render(request, 'note_create.html', context)

@login_required
def note_delete_view(request, id):
    obj = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../../")
    context = {
        "note": obj,
    }
    return render(request, 'note_delete.html', context)

@login_required
def note_create_view(request, taskid=None, projectid=None, actionid=None):
    initial_data = {
        'previous_url' : request.META.get('HTTP_REFERER')
    }
    if taskid:
        initial_data['task'] = taskid
        current_task = Task.objects.filter(id=taskid)
        initial_data['project'] = current_task.project.id
    elif projectid:
        initial_data['project'] = projectid
    elif actionid:
        initial_data['action'] = actionid
        current_action = Action.objects.filter(id=actionid)
        initial_data['task'] = current_action[0].task.id
        initial_data['project'] = current_action[0].task.project.id
    print(initial_data)
    form = NoteCreationForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        previous_ulr = form.cleaned_data['previous_url']
        form_obj = form.save()
        form_obj.updated_at = datetime.datetime.now()
        form_obj.note_updated_by = request.user
        form_obj.note_created_by = request.user
        form_obj.save()
        return redirect(previous_ulr)
    context = {
        "form" : form
    }
    return render(request, 'note_create.html', context)