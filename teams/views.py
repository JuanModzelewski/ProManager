from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django_htmx.http import HttpResponseClientRefresh
from .models import ProjectTeam
from projects.models import Project
from .forms import ProjectTeamForm


def view_project_teams(request, project_id):
    """
    Display a list of teams for the given project.

    **Context:**
    ``project``
        The project that the teams are being displayed for.
    ``project_teams``
        A list of teams belonging to the requested project.
    """
    project = get_object_or_404(Project, pk=project_id)
    project_teams = ProjectTeam.objects.filter(project=project)
    return render(
        request, 'teams/teams.html',
        {'project': project, 'project_teams': project_teams}
    )


def create_project_team(request, project_id):
    """
    Create a new team for the given project.

    **Context:**
    ``project``
        The project that the team is being created for.
    """
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        team_form = ProjectTeamForm(request.POST)
        if team_form.is_valid():
            team = team_form.save(commit=False)
            team.project = project
            team.save()
            team.members.set(
                team_form.cleaned_data['members']
            )
            messages.success(
                request, f"Team <strong> '{team.title}' \
                    </strong> created."
            )
            return HttpResponseClientRefresh()
    else:
        team_form = ProjectTeamForm()
    return render(
        request, "teams/team_modal.html",
        {"project": project, "team_form": team_form}
    )


def edit_project_team(request, project_id, team_id):
    """
    Update an existing team for the given project.

    **Context:**
    ``project``
        The project that the team is being updated for.
    ``project_teams``
        The team that is being updated.
    """
    project = get_object_or_404(Project, pk=project_id)
    project_teams = get_object_or_404(ProjectTeam, pk=team_id)
    if request.method == "POST":
        team_form = ProjectTeamForm(
            request.POST, instance=project_teams
        )
        if team_form.is_valid():
            team_form.save()
            if 'members' in team_form.cleaned_data and \
               team_form.cleaned_data['members']:
                project_teams.members.set(
                    team_form.cleaned_data['members']
                )
                messages.success(
                    request, f"Team <strong> '{project_teams.title}' \
                        </strong> updated."
                )
                return HttpResponseClientRefresh()
            elif not team_form.has_changed():
                return HttpResponseClientRefresh()
    else:
        team_form = ProjectTeamForm(instance=project_teams)
    return render(
        request, "teams/team_modal.html",
        {"project": project, "team_form": team_form,
         "project_teams": project_teams}
    )


def delete_team_members(request, project_id, team_id, member_ids):
    """
    Remove members from the team.

    **Context:**
    ``project``
        The project that the team is being displayed for.
    ``project_teams``
        The team that the members are being removed from.
    ``member_ids``
        The ids of the members that are being removed from the team.
    """
    project = get_object_or_404(Project, pk=project_id)
    project_teams = get_object_or_404(ProjectTeam, pk=team_id)

    if project.author == request.user:
        if member_ids:
            member_ids = member_ids.split(',')
            members = User.objects.filter(id__in=member_ids)
            project_teams.members.remove(*members)
            messages.success(
                request, f"Members removed from team \
                    <strong> '{project_teams.title}' </strong>."
            )
        else:
            messages.error(
                request,
                "No members selected for deletion."
            )
    else:
        messages.error(
            request,
            f"You are not authorized to remove members from this team."
        )

    return HttpResponseRedirect(
        reverse('view_project_teams', args=[project_id])
    )


def delete_project_team(request, project_id, team_id):
    """
    Delete an existing team for the given project.

    **Context:**
    ``project``
        The project that the team is being deleted for.
    ``project_teams``
        The team that is being deleted.
    """
    project = get_object_or_404(Project, pk=project_id)
    project_teams = get_object_or_404(ProjectTeam, pk=team_id)

    if project.author == request.user:
        project_teams.delete()
        messages.success(
            request, f"Team <strong> '{project_teams.title}' \
                </strong> deleted."
        )
    else:
        messages.error(
            request, f"You are not authorized to delete this team."
        )

    return HttpResponseRedirect(
        reverse('view_project_teams', args=[project_id])
    )
