from django.shortcuts import render
from .models import ProjectTeam

# Create your views here.
def project_members(request):
    team_members = ProjectTeam.objects.prefetch_related('project').all()
    return render(request, 'projects/projects.html', {'team_members': team_members})
