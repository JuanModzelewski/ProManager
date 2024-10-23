from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProjectTeam

# Register your models here.

class ProjectTeamAdmin(SummernoteModelAdmin):
    list_display = ('title', 'project')
    list_filter = ('project',)
    search_fields = ['project', 'members']
    list_per_page = 25


admin.site.register(ProjectTeam, ProjectTeamAdmin)