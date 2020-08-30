from django.shortcuts import render, get_object_or_404
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

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Task, id=id_)

