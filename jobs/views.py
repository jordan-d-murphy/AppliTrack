from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Sum

from .models import Job, FollowUp

class JobListView(ListView):
    model = Job
    ordering = ['-applied_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        multiples = Job.objects.filter(multiple=True).aggregate(Sum('multiple_count'))['multiple_count__sum']
        multiples = 0 if multiples is None else multiples
        multi_sub = Job.objects.filter(multiple=True).count()
        add_multiples = multiples - multi_sub
        context['total_jobs'] = Job.objects.count() + add_multiples 
        return context
    
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

