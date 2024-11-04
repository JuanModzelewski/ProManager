from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django_htmx.http import HttpResponseClientRefresh
from .models import ProjectEpic
from tasks.models import ProjectTask
from projects.models import Project
from .forms import ProjectEpicForm


class ProjectEpicsView(generic.ListView):
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
    template_name = "epics/epics.html"
    context_object_name = "project_epics"

    def get_queryset(self):
        """
        Get a list of epics belonging to the requested project.
        """
        project_id = self.kwargs.get("project_id")
        self.project = get_object_or_404(Project, pk=project_id)
        self.epic_tasks = ProjectTask.objects.filter(project=self.project)
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


def create_project_epic(request, project_id):
    """
    Create a new epic for the given project.

    **Context:**
    ``project``
        The project that the epic is being created for.
    """
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        epic_form = ProjectEpicForm(request.POST)
        if epic_form.is_valid():
            epic = epic_form.save(commit=False)
            epic.author = request.user
            epic.project = project
            epic.save()
            messages.success(request,
                             f"The epic <strong> '{epic.title}' \
                                </strong> has been created.")
            return HttpResponseClientRefresh()
    else:
        epic_form = ProjectEpicForm()
    return render(request,
                  "epics/epic_modal.html",
                  {"project": project,
                   "epic_form": epic_form
                   })


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
                         f"The epic <strong> '{epic.title}' \
                            </strong> has been deleted.")
    else:
        messages.error(request,
                       f"You are not authorized to delete this epic.")
    return HttpResponseRedirect(reverse(
        'view_project_epics',
        args=[project_id]))


def edit_project_epic(request, project_id, epic_id):
    """
    Edit an existing epic for the given project.

    **Context:**
    ``project``
        The project that the epic is being updated for.
    ``epic_form``
        A form for updating an existing epic.
    ``epic``
        The epic being updated.
    """
    project = get_object_or_404(Project, pk=project_id)
    epic = get_object_or_404(ProjectEpic, pk=epic_id)
    if request.method == "POST":
        epic_form = ProjectEpicForm(request.POST, instance=epic)
        if epic_form.is_valid():
            epic_form.save()
            messages.success(request,
                             f"The epic <strong> '{epic.title}' \
                                </strong> has been updated.")
            return HttpResponseClientRefresh()
    else:
        epic_form = ProjectEpicForm(instance=epic)
    return render(request,
                  "epics/epic_modal.html",
                  {"project": project,
                   "epic_form": epic_form,
                   "epic": epic
                   })


def view_epic_details(request, project_id, epic_id):
    """
    View the details of an existing epic for the given project.

    **Context:**
    ``project``
        The project that the epic is being displayed for.
    ``epic``
        The epic that is being displayed.
    """
    project = get_object_or_404(Project, pk=project_id)
    epic = get_object_or_404(ProjectEpic, pk=epic_id)
    return render(request,
                  "epics/epic_details.html",
                  {"project": project, "epic": epic}
                  )
