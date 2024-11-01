from . import views
from django.urls import path


urlpatterns = [     
    path("<int:project_id>", views.ProjectEpicsView.as_view(), name="view_project_epics"),
    path("<int:project_id>/epic_modal", views.create_project_epic, name="create_epic"),
    path("delete_epic/<int:project_id>/<int:epic_id>", views.delete_project_epic, name="delete_epic"),
    path("epic_modal/<int:project_id>/<int:epic_id>", views.edit_project_epic, name="edit_epic"),
    path("epic_details/<int:project_id>/<int:epic_id>", views.view_epic_details, name="view_epic_details"),
]
