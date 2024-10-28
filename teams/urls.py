from . import views
from django.urls import path



urlpatterns = [
    path("<int:project_id>", views.view_project_teams, name="view_project_teams"),
    path("team_modal/<int:project_id>", views.create_project_team, name="create_team"),
    path("team_modal/<int:project_id>/<int:team_id>", views.edit_project_team, name="edit_team"),
    path("delete_members/<int:project_id>/<int:team_id>/<str:member_ids>", views.delete_team_members, name="delete_members"),
    
]

