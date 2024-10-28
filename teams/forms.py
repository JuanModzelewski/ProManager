from django import forms
from .models import ProjectTeam
from django.contrib.auth.models import User
from django.db.models import Q




class ProjectTeamForm(forms.ModelForm):
    class Meta:
        model = ProjectTeam
        fields = ['title', 'search_member',]


    search_member = forms.CharField(
        label='Search for a member',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for a member',
            'id': 'member-search-input',
            'class': 'form-control',
        }),
        help_text='You can add more than one member. Separate usernames with commas',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean_search_member(self):
        search_input = self.cleaned_data.get('search_member')
        if search_input:
            usernames = [name.strip() for name in search_input.split(',')]
            members = []
            for username in usernames:
                try:
                    user = User.objects.get(username=username)
                    if self.instance.pk and user in self.instance.members.all():
                        raise forms.ValidationError(
                            f"User '{username}' is already a member of this team."
                        )
                    members.append(user)
                except User.DoesNotExist:
                    raise forms.ValidationError(
                        f"User '{username}' does not exist."
                    )    
            # Get existing members
            existing_members = self.instance.members.all() if self.instance.pk else []
            # Combine new members with existing members
            all_members = list(existing_members) + members
            self.cleaned_data['members'] = User.objects.filter(id__in=[user.id for user in all_members])
            return self.cleaned_data

