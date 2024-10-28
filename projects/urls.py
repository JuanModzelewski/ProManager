from . import views
from django.urls import path, include



urlpatterns = [
    path("", views.ProjectView.as_view(), name="projects"),
    path("project_modal", views.create_project, name="create_project"),
    path("delete_project/<int:project_id>", views.delete_project, name="delete_project"),
    path("project_modal/<int:project_id>", views.edit_project, name="edit_project"),
    path("<int:project_id>", views.project_overview, name="project_overview"),
    path('', include('teams.urls'), name='team'),
    

]