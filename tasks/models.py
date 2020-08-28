from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    assignee = models.ForeignKey (User, related_name="assigned_tasks", on_delete=models.CASCADE, null=True)
    project = models.ForeignKey (Project, related_name="related_project", on_delete=models.CASCADE, null=True)
    completed = models.BooleanField()
    onHold = models.BooleanField()
    priority = models.IntegerField()
    placeInOrder = models.IntegerField()
    duedate = models.DateField()
    owner = models.ForeignKey (User, related_name="owned_tasks", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title