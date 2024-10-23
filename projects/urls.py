from . import views
from django.urls import path



urlpatterns = [
    path("", views.ProjectView.as_view(), name="project"),
    path("create_project", views.create_project, name="create_project"),

]