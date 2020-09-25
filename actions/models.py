from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task
from django.urls import reverse

# Create your models here.

class Action(models.Model):
    title = models.CharField(max_length=200)
    task = models.ForeignKey (Task, related_name="related_task", on_delete=models.CASCADE, null=True)
    assignee = models.ForeignKey (User, related_name="assigned_actions", on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey (User, related_name="owned_actions", on_delete=models.CASCADE, null=True)
    duedate = models.DateField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    onHold = models.BooleanField(default=False)
    priority = models.IntegerField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("actions:action_detail_view", kwargs={"id": self.id})