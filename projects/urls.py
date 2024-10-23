from . import views
from django.urls import path



urlpatterns = [
    path("", views.ProjectView.as_view(), name="project"),
]