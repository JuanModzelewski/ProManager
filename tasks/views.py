from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
import django_filters
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django_htmx.http import HttpResponseClientRefresh
from .models import ProjectTask
from projects.models import Project
from teams.models import ProjectTeam
from .forms import ProjectTaskForm, TaskStatusForm


class TaskListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ProjectTask
        fields = ['assignee']

class TaskList(generic.ListView):
    model = ProjectTask
    template_name = 'tasks/tasks.html'
    context_object_name = 'project_tasks'

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        project = get_object_or_404(Project, pk=project_id)

        if self.request.GET.get('filter') == 'my_team':
            return ProjectTask.objects.filter(project=project, assignee__members=self.request.user)
        else:
            return ProjectTask.objects.filter(project=project)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=self.kwargs['project_id'])
        context['task_form'] = ProjectTaskForm(project=context['project'])
        context['status_form'] = TaskStatusForm()
        return context


def create_project_task(request, project_id):
    """Create a new task for the given project."""
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        task_form = ProjectTaskForm(request.POST or None, project=project)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.author = request.user
            task.project = project
            task.save()
            messages.success(request, f"Task '{task.title}' created.")
            return HttpResponseClientRefresh()
    else:
        task_form = ProjectTaskForm()
    return render(request, 'tasks/task_modal.html', {'task_form': task_form, 'project': project})


def edit_project_task(request, project_id, task_id):
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(ProjectTask, pk=task_id)

    if request.method == "POST":
        task_form = ProjectTaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, f"Task '{task.title}' updated.")
            return HttpResponseClientRefresh()
    else:
        task_form = ProjectTaskForm(instance=task)
    return render(request, 'tasks/task_modal.html', {'task_form': task_form, 'project': project, 'task': task})


def update_task_status(request, project_id, task_id):
    task = get_object_or_404(ProjectTask, pk=task_id)

    if request.method == "POST":
        status_form = TaskStatusForm(request.POST, instance=task)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, f"Task '{task.title}' status updated.")
            return HttpResponseClientRefresh()
    else:
        status_form = TaskStatusForm(instance=task)
    return HttpResponseRedirect(reverse('view_project_tasks', kwargs={'project_id': project_id}))


def delete_project_task(request, project_id, task_id):
    task = get_object_or_404(ProjectTask, pk=task_id)
    if task.author == request.user:
        task.delete()
        messages.success(request, f"Task '{task.title}' deleted.")
        return HttpResponseRedirect(reverse('view_project_tasks', kwargs={'project_id': project_id}))
    else:
        messages.error(request, f"You are not authorized to delete this task.")
        return HttpResponseRedirect(reverse('view_project_tasks', kwargs={'project_id': project_id}))

    

