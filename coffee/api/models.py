from django.db import models
from jsonfield import JSONField

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=255),
    description = models.TextField(),
    location = JSONField(),
    images =  JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
