from django.db import models
from django.utils import timezone
from datetime import timedelta


# Create your models here.



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    task_start_date = models.DateField(default=timezone.localdate)
    task_end_date = models.DateField(default=timezone.localdate() + timedelta(days=7))
    completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title