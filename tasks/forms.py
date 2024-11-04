from django import forms
from .models import ProjectTask
from epics.models import ProjectEpic
from teams.models import ProjectTeam


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = ProjectTask
        fields = ['title', 'description', 'status', 'assignee', 'epic']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 8,
                'style': 'height: 200px;',
                'class': 'form-control'
                }),
            'status': forms.Select(attrs={
                'class': 'form-select form-control',
                'style': 'width: 100%;'
                }),
            'assignee': forms.Select(attrs={
                'class': 'form-select form-control',
                'style': 'width: 100%;'
                }),
            'epic': forms.Select(attrs={
                'class': 'form-select form-control',
                'style': 'width: 100%;'
                }),
        }

    def __init__(self, *args, **kwargs):
        """
        Add the requested project to the form.
        Custom widgets for the assignee and epic fields.
        Ensures that the assignee field only shows members of the project.
        Ensures that the epic field only shows epics of the project.
        """
        project = kwargs.pop('project', None)
        super().__init__(*args, **kwargs)
        if project:
            self.fields['epic'].queryset = \
                ProjectEpic.objects.filter(project=project)
            self.fields['assignee'].queryset = \
                ProjectTeam.objects.filter(project=project)
            self.fields['assignee'].label_from_instance = \
                self.assignee_label

    def assignee_label(self, obj):
        """
        Return a string representation of the task assignee.
        Used in the label_from_instance method.
        """
        member_names = ", ".join(
            [member.username for member in obj.members.all()])
        return f"{obj.title} | Members: {member_names}"


class TaskStatusForm(forms.ModelForm):
    class Meta:
        """
        Add the requested project to the form.
        Custom widgets for the status field.
        """
        model = ProjectTask
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select form-control',
                'placeholder': 'Status',
                'style': 'width: 200px;',
            }),
        }
