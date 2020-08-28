from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    closed = models.BooleanField(default=False)
    onHold = models.BooleanField(default=False)
    priority = models.IntegerField(blank=True)
    placeInOrder = models.IntegerField(blank=True)
    duedate = models.DateField(blank=True)
    owner = models.ForeignKey (User, related_name="owned_projects", on_delete=models.CASCADE, null=True, blank=True)
    assignee = models.ForeignKey (User, related_name="assigned_projects", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title