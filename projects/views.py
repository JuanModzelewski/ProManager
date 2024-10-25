from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django_htmx.http import HttpResponseClientRefresh
from .models import Project, ProjectTeam
from .forms import ProjectForm


# Create your views here.
class ProjectView(generic.ListView):
    template_name = "projects/projects.html"
    
    def get_queryset(self):
        return Project.objects.filter(Q(author=self.request.user) | Q(projectteam__members=self.request.user)).distinct()
    


def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid() and request.user.is_authenticated:
            new_project = project_form.save(commit=False)
            new_project.author = request.user
            new_project.save()
            messages.success(request, f"The project <strong> {new_project.title} </strong> has been created.")
            return HttpResponseClientRefresh()
    else:
        project_form = ProjectForm()
    return render(request, 'projects/project_modal.html', {'project_form': project_form})


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.author == request.user:
        project.delete()
        messages.success(request, f"The project <strong> {project.title} </strong> has been deleted.")
        return HttpResponseRedirect(reverse('projects'))
    else:
        messages.error(request, f"You are not authorized to delete this project.")
        return HttpResponseRedirect(reverse('projects'))
        
  

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.author == request.user:
        if request.method == "POST":
            project_form = ProjectForm(request.POST, instance=project)
            if project_form.is_valid():
                project_form.save()
                messages.success(request, f"The project <strong> {project.title} </strong> has been updated.")
                return HttpResponseClientRefresh()
        else:
            project_form = ProjectForm(instance=project)
        return render(request, 'projects/project_modal.html', {'project_form': project_form})
    else:
        messages.error(request, f"You are not authorized to edit this project.")
        return HttpResponseRedirect(reverse('projects'))




