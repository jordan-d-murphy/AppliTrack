import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    applied_date = models.DateTimeField("date applied", default=datetime.datetime.now())
    favorite = models.BooleanField()

    def __str__(self):
        return f"{self.title} @ {self.company}"
    
    def recently_applied(self):
        return self.applied_date >= timezone.now() - datetime.timedelta(days=3)
    
    def get_absolute_url(self):
      return reverse("jobs:job_detail", kwargs={"pk": self.pk})

class FollowUp(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField("date added", default=datetime.datetime.now())
    due_date = models.DateTimeField("due date", blank=True)
    resolved = models.BooleanField()

    def __str__(self):
        return f"{self.name} | {self.description} ({self.job})"
    
    def upcoming(self):
        return self.due_date <= timezone.now() + datetime.timedelta(days=3)
    
    def get_absolute_url(self):
      return reverse("follow_up_detail", kwargs={"pk": self.pk})

