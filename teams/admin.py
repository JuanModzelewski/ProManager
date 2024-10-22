from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProjectTeam

# Register your models here.

class ProjectTeamAdmin(SummernoteModelAdmin):
    list_display = ('team_title', 'project')
    list_filter = ('project',)
    search_fields = ['team_members__username', 'project__title']
    list_per_page = 25


admin.site.register(ProjectTeam, ProjectTeamAdmin)