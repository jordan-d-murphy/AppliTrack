import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    applied_date = models.DateTimeField("date applied")
    favorite = models.BooleanField()

    def __str__(self):
        return f"{self.title} @ {self.company}"
    
    def recently_applied(self):
        return self.applied_date >= timezone.now() - datetime.timedelta(days=3)

class FollowUp(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    created_date = models.DateTimeField("date added")
    due_date = models.DateTimeField("due date")
    resolved = models.BooleanField()

    def __str__(self):
        return f"{self.name} | {self.description} ({self.job})"
    
    def upcoming(self):
        return self.due_date <= timezone.now() + datetime.timedelta(days=3)
