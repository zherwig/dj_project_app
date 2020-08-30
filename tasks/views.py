from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Task

# Create your views here.

class TaskListView(ListView):
    template_name = 'task_list.html'
    queryset = Task.objects.all()

class TaskDetailView(DetailView):
    template_name = 'task_detail.html'
    queryset = Task.objects.all()

