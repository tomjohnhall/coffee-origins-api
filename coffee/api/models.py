from django.db import models
from jsonfield import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=255, default='')
    type = models.CharField(max_length=255, default='')
    roaster = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    region = models.CharField(max_length=255, blank=True)
    grower = models.CharField(max_length=255, blank=True)
    process = models.CharField(max_length=255, blank=True)
    tasting = JSONField(null=True)
    shopURL = models.URLField(max_length=255, blank=True)
    last_in = models.DateTimeField(null=True)
    next_in = models.DateTimeField(null=True)
    location = JSONField(null=True)
    images = JSONField(null=True)
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
