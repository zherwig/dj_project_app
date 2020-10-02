from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Note
from tasks.models import Task
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
    initial_data = {}
    if taskid:
        initial_data['task'] = taskid
    elif projectid:
        initial_data['project'] = projectid
    elif actionid:
        initial_data['action'] = actionid
    form = NoteCreationForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        print("Form valid")
        form_obj = form.save()
        form_obj.updated_at = datetime.datetime.now()
        form_obj.note_updated_by = request.user
        form_obj.note_created_by = request.user
        form_obj.save()
        form = NoteCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'note_create.html', context)