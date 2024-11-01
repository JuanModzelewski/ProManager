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



class ProjectTeamsView(generic.UpdateView):
    model = ProjectTeam
    template_name = 'teams/teams.html'
    form_class = ProjectTeamForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
        

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
    project_teams = get_object_or_404(ProjectTeam, pk=team_id)

    if request.method == "POST":
        team_form = ProjectTeamForm(request.POST, instance=project_teams)
        if team_form.is_valid():
            team_form.save()
            if 'members' in team_form.cleaned_data and team_form.cleaned_data['members']:
                project_teams.members.set(team_form.cleaned_data['members'])
                messages.success(request, f"Team '{project_teams.title}' updated.")
                return HttpResponseClientRefresh()
            elif not team_form.has_changed():
                return HttpResponseClientRefresh()
    else:
        team_form = ProjectTeamForm(instance=project_teams)

    return render(request, "teams/team_modal.html", {"project": project, "team_form": team_form, "project_teams": project_teams})


def delete_team_members(request, project_id, team_id, member_ids):
    project = get_object_or_404(Project, pk=project_id)
    project_teams = get_object_or_404(ProjectTeam, pk=team_id)

    if project_teams.project.author == request.user:
        member_ids = member_ids.split(',')
        members = User.objects.filter(id__in=member_ids)
        project_teams.members.remove(*members)
        messages.success(request, f"Members removed from team '{project_teams.title}'.")
        return HttpResponseRedirect(reverse('view_project_teams', kwargs={'project_id': project.id}))
    else:
        messages.error(request, f"You are not authorized to delete members from this team.")
        return HttpResponseRedirect(reverse('view_project_teams', kwargs={'project_id': project.id}))


def delete_team(request, project_id, team_id):
    project = get_object_or_404(Project, pk=project_id)
    project_teams = get_object_or_404(ProjectTeam, pk=team_id)
    project_teams.delete()
    messages.success(request, f"Team '{project_teams.title}' deleted.")
    return HttpResponseRedirect(reverse('view_project_teams', kwargs={'project_id': project.id}))
    
    

