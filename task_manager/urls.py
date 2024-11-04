from . import views
from django.urls import path


urlpatterns = [
    path("<int:project_id>/",
         views.TaskManager.as_view(),
         name="task_manager"
         ),
    path("<int:project_id>/delete_task/<int:task_id>",
         views.delete_project_task,
         name="delete_task"
         ),
    path("<int:project_id>/delete_epic/<int:epic_id>",
         views.delete_project_epic,
         name="delete_epic"
         ),
]
