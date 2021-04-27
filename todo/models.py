from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=255, unique=True)
    task_desc = models.CharField(max_length=255)
    task_deadline = models.DateField(auto_now=False, auto_now_add=False)

    objects = models.Manager()
