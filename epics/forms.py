from django import forms
from .models import ProjectEpic
from django import forms


class ProjectEpicForm(forms.ModelForm):
    class Meta:
        model = ProjectEpic
        fields = ['title', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'style': 'width: 100%;'}),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'style': 'width: 100%;'}),
            'description': forms.Textarea(
                attrs={'rows': 8,
                       'style': 'height: 200px;',
                       'class': 'form-control'
                       }),
        }
