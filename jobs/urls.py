from django.urls import path

from jobs.views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView 
from jobs.views import FollowUpListView, FollowUpDetailView, FollowUpCreateView, FollowUpUpdateView, FollowUpDeleteView

app_name = "jobs"

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/create/', JobCreateView.as_view(), name='job_create'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),

    path('follow_ups', FollowUpListView.as_view(), name='follow_ups_list'),
    path('follow_ups/<int:pk>/', FollowUpDetailView.as_view(), name='follow_ups_detail'),
    path('follow_ups/create/', FollowUpCreateView.as_view(), name='follow_ups_create'),
    path('follow_ups/<int:pk>/update/', FollowUpUpdateView.as_view(), name='follow_ups_update'),
    path('follow_ups/<int:pk>/delete/', FollowUpDeleteView.as_view(), name='follow_ups_delete'),
]

