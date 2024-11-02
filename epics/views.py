from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django_htmx.http import HttpResponseClientRefresh
from .models import ProjectEpic
from tasks.models import ProjectTask
from projects.models import Project
from .forms import ProjectEpicForm


# Create your views here.
class ProjectEpicsView(generic.ListView):
    """
    View for displaying a list of epics belonging to a project.
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
        return ProjectEpic.objects.filter(project=self.project)

    def get_context_data(self, **kwargs):
        """
        Add the requested project to the context.
        """
        context = super().get_context_data(**kwargs)
        context["project"] = self.project
        return context


def create_project_epic(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        epic_form = ProjectEpicForm(request.POST)
        if epic_form.is_valid():
            epic = epic_form.save(commit=False)
            epic.author = request.user
            epic.project = project
            epic.save()
            messages.success(request, f"The epic '{epic.title}' has been created.")
            return HttpResponseClientRefresh()
    else:
        epic_form = ProjectEpicForm()

    return render(request, "epics/epic_modal.html", {"project": project, "epic_form": epic_form})


def delete_project_epic(request, project_id, epic_id):
    project = get_object_or_404(Project, pk=project_id)
    epic = get_object_or_404(ProjectEpic, pk=epic_id)

    if project.author == request.user:
        epic.delete()
        messages.success(request, f"The epic '{epic.title}' has been deleted.")
        return HttpResponseRedirect(reverse('view_project_epics', kwargs={'project_id': project.id}))
    else:
        messages.error(request, f"You are not authorized to delete this epic.")
        return HttpResponseRedirect(reverse('view_project_epics', kwargs={'project_id': project.id}))
    

def edit_project_epic(request, project_id, epic_id):
    project = get_object_or_404(Project, pk=project_id)
    epic = get_object_or_404(ProjectEpic, pk=epic_id)

    if request.method == "POST":
        epic_form = ProjectEpicForm(request.POST, instance=epic)
        if epic_form.is_valid():
            epic_form.save()
            messages.success(request, f"The epic '{epic.title}' has been updated.")
            return HttpResponseClientRefresh()
    else:
        epic_form = ProjectEpicForm(instance=epic)

    return render(request, "epics/epic_modal.html", {"project": project, "epic_form": epic_form, "epic": epic})


def view_epic_details(request, project_id, epic_id):
    project = get_object_or_404(Project, pk=project_id)
    epic = get_object_or_404(ProjectEpic, pk=epic_id)
    return render(request, "epics/epic_details.html", {"project": project, "epic": epic})
