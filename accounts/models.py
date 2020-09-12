from django.db import models
from django.contrib.auth.models import User


#needed for create_user_profile and save_user_profile 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    #creating relation to built in model 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #extra fields
    role = models.TextField(max_length=200, blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()