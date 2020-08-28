from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True)
    closed = models.BooleanField()
    onHold = models.BooleanField()
    priority = models.IntegerField()
    placeInOrder = models.IntegerField()
    duedate = models.DateField()
    owner = models.ForeignKey (User, related_name="owned_projects", on_delete=models.CASCADE, null=True)
    assignee = models.ForeignKey (User, related_name="assigned_projects", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title