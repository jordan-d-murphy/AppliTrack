from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .models import Job, FollowUp

class JobListView(ListView):
    model = Job
    ordering = ['-applied_date']

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

