from django.shortcuts import get_object_or_404, render

from .models import Job, FollowUp

# Create your views here.
def index(request):
    latest_jobs_list = Job.objects.order_by("-applied_date")[:5]
    context = {
        "latest_jobs_list": latest_jobs_list,
    }
    return render(request, "jobs/index.html", context)

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, "jobs/detail.html", {"job": job})
