from . import views
from django.urls import path


urlpatterns = [
    path("<int:project_id>/",
         views.TaskList.as_view(),
         name="view_project_tasks"
         ),
    path("<int:project_id>/create",
         views.create_project_task,
         name="create_task"
         ),
    path("<int:project_id>/tasks/<int:task_id>",
         views.edit_project_task,
         name="edit_task"
         ),
    path("<int:project_id>/tasks/<int:task_id>/update_status",
         views.update_task_status,
         name="update_status"),
    path("<int:project_id>/delete_task/<int:task_id>",
         views.delete_project_task,
         name="delete_task"
         ),
]
