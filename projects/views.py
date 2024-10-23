from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.db.models import Q
from django.views import generic
from django.contrib import messages
from itertools import chain
from .models import Project, ProjectTeam
from .forms import ProjectForm


# Create your views here.
class ProjectView(generic.ListView):
    template_name = "projects/projects.html"
    
    def get_queryset(self):
        return Project.objects.filter(Q(author=self.request.user) | Q(projectteam__members=self.request.user)).distinct()
    


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            new_project = form.save(commit=False)
            new_project.author = request.user
            new_project.save()
            messages.success(request, f"{new_project.title} added.")
            return redirect('project')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

