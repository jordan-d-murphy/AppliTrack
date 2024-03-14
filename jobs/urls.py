from django.urls import path

from jobs.views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView

app_name = "jobs"

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/create/', JobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
]

