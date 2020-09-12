from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
from tasks.models import Task
from actions.models import Action
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_text = models.TextField(blank=True, null=True)
    archived = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    project = models.ForeignKey (Project, related_name="note_project_relation", on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey (Task, related_name="note_task_relation", on_delete=models.CASCADE, null=True, blank=True)
    action = models.ForeignKey (Action, related_name="note_action_relation", on_delete=models.CASCADE, null=True, blank=True)
    note_created_by = models.ForeignKey (User, related_name="created_by", on_delete=models.CASCADE, null=True, blank=True)
    note_updated_by = models.ForeignKey (User, related_name="updated_by", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.note_title
    
    def get_absolute_url(self):
        return reverse("notes:note_detail_view", kwargs={"id": self.id})