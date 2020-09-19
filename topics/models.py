from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("topics:topic_detail_view", kwargs={"id": self.id})