from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from epics.models import ProjectEpic
from tasks.models import ProjectTask
from projects.models import Project


class TaskManager(generic.ListView):
    """
    View for displaying a list of epics belonging to a project.

    **Context:**
    ``project``
        The project that the epics are being displayed for.
    ``project_epics``
        A list of epics belonging to the requested project.
    """
    model = ProjectEpic
    project_epics = ProjectEpic.objects.all()
    epic_tasks = ProjectTask.objects.all()
    template_name = "task_manager/task_manager.html"
    context_object_name = "task_manager"

    def get_queryset(self):
        """
        Get a list of epics belonging to the requested project.
        """
        project_id = self.kwargs.get("project_id")
        self.project = get_object_or_404(
            Project, pk=project_id)
        self.epic_tasks = ProjectTask.objects.filter(
            project=self.project)
        return ProjectEpic.objects.filter(
            project=self.project).order_by("start_date")

    def get_context_data(self, **kwargs):
        """
        Add the requested project to the context.
        """
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        context["project_epics"] = self.get_queryset()
        return context


def delete_project_task(request, project_id, task_id):
    """
    Delete an existing task for the given project.

    **Context:**
    ``project``
        The project that the task is being deleted for.
    ``task``
        The task that is being deleted.
    """
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(ProjectTask, pk=task_id)
    if task.author == request.user:
        task.delete()
        messages.success(request,
                         f"Task <strong>' {task.title}' \
                            </strong> has been deleted.")
    else:
        messages.error(request,
                       f"You are not authorized to delete this task.")
    return HttpResponseRedirect(reverse(
        "task_manager", args=[project_id]))


def delete_project_epic(request, project_id, epic_id):
    """
    Delete an existing epic for the given project.

    **Context:**
    ``project``
        The project that the epic is being deleted for.
    ``epic``
        The epic that is being deleted.
    """
    project = get_object_or_404(Project, pk=project_id)
    epic = get_object_or_404(ProjectEpic, pk=epic_id)
    if project.author == request.user:
        epic.delete()
        messages.success(request,
                         f"The epic <strong>' {epic.title}' \
                            </strong> has been deleted.")
    else:
        messages.error(request,
                       f"You are not authorized to delete this epic.")
    return HttpResponseRedirect(reverse(
        'task_manager', args=[project_id]))
