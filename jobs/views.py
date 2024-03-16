from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Job, FollowUp

class JobListView(ListView):
    model = Job
    ordering = ['-applied_date']

    def get_queryset(self):
        # http://127.0.0.1:8000/jobs/?search=DoorDash
        query = self.request.GET.get('search')
        if query is not None:
            if query == "favorite":
                return Job.objects.filter(favorite=True)
            return Job.objects.filter(company__icontains=query).order_by('-applied_date')
        return Job.objects.filter().order_by('-applied_date')
    
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

