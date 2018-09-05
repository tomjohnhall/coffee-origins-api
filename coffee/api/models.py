from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = JSONField()
    images = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coffees = models.ManyToManyField(Coffee, related_name="list", blank=True, null=True)
    favourites = models.ManyToManyField(Coffee, related_name="favourite", blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
