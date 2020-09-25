from django.db import models
from django.contrib.auth.models import User
from topics.models import Topic
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)
    topic = models.ForeignKey (Topic, related_name="related_topic", on_delete=models.CASCADE, null=True, blank=True)
    closed = models.BooleanField(default=False)
    onHold = models.BooleanField(default=False)
    priority = models.IntegerField(blank=True, null=True)
    placeInOrder = models.IntegerField(blank=True, null=True)
    duedate = models.DateField(blank=True, null=True)
    owner = models.ForeignKey (User, related_name="owned_projects", on_delete=models.CASCADE, null=True, blank=True)
    assignee = models.ForeignKey (User, related_name="assigned_projects", on_delete=models.CASCADE, null=True, blank=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("projects:project_detail_view", kwargs={"id": self.id})
    