from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProjectTask


class ProjectTaskAdmin(SummernoteModelAdmin):
    list_display = ('title', 'project', 'epic', 'author', 'assignee', 'status', 'created', 'updated')
    list_filter = ('project', 'epic', 'assignee', 'status')
    search_fields = ['project', 'epic', 'title', 'assignee', 'status']
    list_per_page = 25

admin.site.register(ProjectTask, ProjectTaskAdmin)