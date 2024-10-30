from django import forms
from .models import ProjectEpic
from django.contrib.auth.models import User
from django.db.models import Q

class ProjectEpicForm(forms.ModelForm):
    class Meta:
        model = ProjectEpic
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    