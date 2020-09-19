from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from topics.models import Topic
from tasks.models import Task
from topics.forms import TopicCreationForm
from django.contrib.auth.models import User
import datetime

# Create your views here.
def topics_list_view(request, *args, **kwargs):
    context = {
        "topics": Topic.objects.all(),
        "page_title": "Open topics",
        "user":request.user,
    }
    
    return render(request, 'topics_list.html', context) 

def topic_detail_view(request, id):
    obj = get_object_or_404(Topic, id=id)
    context = {
        "topic": obj,
    }
    return render(request, 'topic_detail.html', context)

def topic_update_view(request, id):
    obj = get_object_or_404(Topic, id=id)
    form = TopicCreationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form_obj = form.save()
        form_obj.updated_at = datetime.datetime.now()
        form_obj.save()
        form = TopicCreationForm()
        return redirect("../")
    context = {
        "form" : form
    }
    return render(request, 'topic_create.html', context)

def topic_delete_view(request, id):
    obj = get_object_or_404(Topic, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../")
    context = {
        "topic": obj,
    }
    return render(request, 'topic_delete.html', context)

def topic_create_view(request):
    form = TopicCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TopicCreationForm()
    context = {
        "form" : form
    }
    return render(request, 'topic_create.html', context)