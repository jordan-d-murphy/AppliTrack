from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Job, FollowUp

class JobListView(ListView):
    model = Job
    ordering = ['-applied_date']

    def get_queryset(self):
        # http://127.0.0.1:8000/jobs/?search=DoorDash
        return Job.objects.filter(company=self.request.GET.get('search'))
    
class FavoriteJobListView(ListView):
    model = Job
    ordering = ['-applied_date']

    def get_queryset(self):
        return Job.objects.filter(favorite=True)
    
class JobDetailView(DetailView):
    model = Job

class JobCreateView(CreateView):
    model = Job
    fields = '__all__'

class JobUpdateView(UpdateView):
    model = Job
    fields = '__all__'

class JobDeleteView(DeleteView):
    model = Job
    success_url = '/jobs'



class FollowUpListView(ListView):
    model = FollowUp
    ordering = ['-created_date']

class FollowUpDetailView(DetailView):
    model = FollowUp

class FollowUpCreateView(CreateView):
    model = FollowUp
    fields = '__all__'

class FollowUpUpdateView(UpdateView):
    model = FollowUp
    fields = '__all__'

class FollowUpDeleteView(DeleteView):
    model = FollowUp
    success_url = '/jobs/follow_ups'

