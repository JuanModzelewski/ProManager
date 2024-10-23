from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Project, ProjectTeam

# Create your views here.
class ProjectView(generic.ListView):
    template_name = "projects/projects.html"

    def get_queryset(self):
        return ProjectTeam.objects.filter(members=self.request.user)
    
