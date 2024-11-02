from . import views
from django.urls import path



urlpatterns = [
    path("<int:project_id>/", views.view_project_teams, name="view_project_teams"),
    path("<int:project_id>/create/", views.create_project_team, name="create_team"),
    path("<int:project_id>/edit/<int:team_id>", views.edit_project_team, name="edit_team"),
    path("<int:project_id>/delete_members/<int:team_id>/<str:member_ids>", views.delete_team_members, name="delete_members"),
    path("<int:project_id>/delete/<int:team_id>", views.delete_team, name="delete_team"),
]
