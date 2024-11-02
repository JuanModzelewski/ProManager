from django import forms
from .models import ProjectTask
from django.contrib.auth.models import User
from django.db.models import Q
from epics.models import ProjectEpic
from teams.models import ProjectTeam


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields = ['title', 'description', 'status', 'assignee', 'epic']

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super().__init__(*args, **kwargs)
        if project is not None:
            self.fields['epic'].queryset = ProjectEpic.objects.filter(project=project)
            self.fields['assignee'].queryset = ProjectTeam.objects.filter(project=project)
            self.fields['assignee'].label_from_instance = self.assignee_label
        

    def assignee_label(self, project_team):
        member_usernames = ", ".join(member.username for member in project_team.members.all())
        return f"{project_team.title} | Members: {member_usernames}"
    

class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select form-control me-3',
                'placeholder': 'Status',
                'style': 'width: 200px;',
            }),
        }

