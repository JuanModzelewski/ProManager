from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django_htmx.http import HttpResponseClientRefresh
from .models import ProjectTeam
from projects.models import Project
from .forms import ProjectTeamForm



# Create your views here.
def view_project_teams(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project_teams = ProjectTeam.objects.filter(project=project)
    
    return render(request, 'teams/teams.html', {'project': project, 'project_teams': project_teams})

def create_project_team(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        team_form = ProjectTeamForm(request.POST)
        if team_form.is_valid():
            team = team_form.save(commit=False)
            team.project = project
            team.save()
            team.members.set(team_form.cleaned_data['members'])
            messages.success(request, f"Team '{team.title}' created.")
            return HttpResponseClientRefresh()
    else:
        team_form = ProjectTeamForm()

    return render(request, "teams/team_modal.html", {"project": project, "team_form": team_form})


def edit_project_team(request, project_id, team_id):
    project = get_object_or_404(Project, pk=project_id)
    team = get_object_or_404(ProjectTeam, pk=team_id)

    if request.method == "POST":
        team_form = ProjectTeamForm(request.POST, instance=team)
        if team_form.is_valid():
            team_form.save()
            if 'members' in team_form.cleaned_data and team_form.cleaned_data['members']:
                team.members.set(team_form.cleaned_data['members'])
            messages.success(request, f"Team '{team.title}' updated.")
            return HttpResponseClientRefresh()
    else:
        team_form = ProjectTeamForm(instance=team)

    return render(request, "teams/team_modal.html", {"project": project, "team_form": team_form, "team": team})


def delete_team_members(request, project_id, team_id, member_ids):
    project = get_object_or_404(Project, pk=project_id)
    team = get_object_or_404(ProjectTeam, pk=team_id)
    member_ids = member_ids.split(',')
    members = User.objects.filter(id__in=member_ids)
    team.members.remove(*members)
    messages.success(request, f"Members removed from team '{team.title}'.")
    return HttpResponseRedirect(reverse('view_project_teams', kwargs={'project_id': project.id}))
    
    

