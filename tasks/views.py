from django.shortcuts import render, get_object_or_404, reverse
import django_filters
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django_htmx.http import HttpResponseClientRefresh
from .models import ProjectTask
from projects.models import Project
from .forms import ProjectTaskForm, TaskStatusForm


class TaskListFilter(django_filters.FilterSet):
    """
    Filter tasks based on the 'filter' GET parameter.
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ProjectTask
        fields = ['assignee']


class TaskList(generic.ListView):
    """
    View for displaying a list of tasks belonging to a project.

    **Context:**
    ``project_tasks``
        A list of tasks belonging to the requested project.
    ``project``
        The project that the tasks are being displayed for.
    """
    model = ProjectTask
    template_name = 'tasks/tasks.html'
    context_object_name = 'project_tasks'

    def get_queryset(self):
        """
        Get a list of tasks belonging to the requested project.
        **Context:**
        ``project``
            The project that the tasks are being displayed for.
        """
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, pk=project_id)

        """
        Filter tasks based on the 'filter' GET parameter.
        """
        if self.request.GET.get('filter') == 'my_team':
            return ProjectTask.objects.filter(
                project=project, assignee__members=self.request.user
            )
        else:
            return ProjectTask.objects.filter(project=project)

    def get_context_data(self, **kwargs):
        """
        Add the requested project to the context.
        **Context:**
        ``project``
            The project that the tasks are being displayed for.
        ``task_form``
            A form for creating a new task.
        ``status_form``
            A form for updating the status of an existing task.
        """
        context = super().get_context_data(**kwargs)
        context["project"] = get_object_or_404(
            Project, pk=self.kwargs['project_id']
        )
        context["task_form"] = ProjectTaskForm(project=context["project"])
        context["status_form"] = TaskStatusForm()
        return context


def create_project_task(request, project_id):
    """
    Create a new task for the given project.

    **Context:**
    ``task_form``
        A form for creating a new task.
    ``project``
        The project that the task is being created for.
    """
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        task_form = ProjectTaskForm(request.POST, project=project)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.project = project
            task.save()
            messages.success(request, f"Task <strong> '{task.title}' \
                             </strong> created.")
            return HttpResponseClientRefresh()
    else:
        task_form = ProjectTaskForm(project=project)
    return render(
        request, 'tasks/task_modal.html',
        {'task_form': task_form, 'project': project}
    )


def edit_project_task(request, project_id, task_id):
    """
    Update an existing task for the given project.

    **Context:**
    ``task_form``
        A form for updating an existing task.
    ``project``
        The project that the task is being updated for.
    ``task``
        The task that is being updated.
    """
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(ProjectTask, pk=task_id)
    if request.method == "POST":
        task_form = ProjectTaskForm(
            request.POST, instance=task, project=project
        )
        if task_form.is_valid():
            task_form.save()
            messages.success(request, f"Task <strong> '{task.title}' \
                             </strong> updated.")
            return HttpResponseClientRefresh()
    else:
        task_form = ProjectTaskForm(instance=task, project=project)
    return render(
        request, 'tasks/task_modal.html',
        {'task_form': task_form, 'project': project, 'task': task}
    )


def update_task_status(request, project_id, task_id):
    """
    Update the status of an existing task for the given project.

    **Context:**
    ``status_form``
        A form for updating the status of an existing task.
    ``project``
        The project that the task is being updated for.
    ``task``
        The task that is being updated.
    """
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(ProjectTask, pk=task_id)

    if request.method == "POST":
        status_form = TaskStatusForm(request.POST, instance=task)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, f"Task <strong> '{task.title}' \
                             </strong> status updated.")
            return HttpResponseClientRefresh()
    else:
        status_form = TaskStatusForm(instance=task)
    return HttpResponseRedirect(reverse(
        'view_project_tasks', args=[project_id]))


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
        messages.success(request, f"Task <strong> '{task.title}' \
                         </strong> deleted.")
    else:
        messages.error(request,
                       f"You are not authorized to delete this task.")
    return HttpResponseRedirect(reverse(
        'view_project_tasks', args=[project_id]))
