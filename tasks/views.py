from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Task
from .forms import TaskModelForm
from django.urls import reverse

# Create your views here.
class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskModelForm #define form to use
    queryset = Task.objects.all()
    success_url = "/tasks/"

class TaskListView(ListView):
    template_name = 'task_list.html'
    queryset = Task.objects.all()

class TaskDetailView(DetailView):
    template_name = 'task_detail.html'
    queryset = Task.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Task, id=id_)

class TaskUpdateView(UpdateView):
    template_name = 'task_create.html'
    form_class = TaskModelForm #define form to use
    queryset = Task.objects.all()
    success_url = "/tasks/"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Task, id=id_)

class TaskDeleteView(DeleteView):
    template_name = 'task_delete.html'
    queryset = Task.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Task, id=id_)
    
    def get_success_url(self):
        return reverse('tasks:task_list_view')