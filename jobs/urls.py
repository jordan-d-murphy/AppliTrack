from django.urls import path

from . import views

app_name = "jobs"

urlpatterns = [
    # ex: /jobs/
    path("", views.index, name="index"),
    # ex: /jobs/5/
    path("<int:job_id>/", views.detail, name="detail"),
]

