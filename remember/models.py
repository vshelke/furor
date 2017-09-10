from django.db import models
from django.conf import settings

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=128)
    img = models.CharField(max_length=256)
    desc = models.TextField(max_length=512)
    link = models.URLField()
    tag = models.CharField(max_length=20)
    completed = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
