from . import views
from django.urls import path



urlpatterns = [
    path("", views.ProjectView.as_view(), name="projects"),
    path("project_modal", views.create_project, name="create_project"),
    path("delete_project/<int:project_id>", views.delete_project, name="delete_project"),
    path("project_modal/<int:project_id>", views.edit_project, name="edit_project"),

]