from . import views
from django.urls import path


urlpatterns = [     
    path("<int:project_id>", views.ProjectEpicsView.as_view(), name="view_project_epics"),
    path("<int:project_id>/epic_modal", views.create_project_epic, name="create_epic"),
]
