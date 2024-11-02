from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProjectTask
from django.utils.dateformat import format

# Register your models here.

class ProjectTaskAdmin(SummernoteModelAdmin):
    list_display = ('title', 'project', 'epic', 'author', 'assignee', 'status', 'created', 'updated')
    list_filter = ('project', 'epic', 'assignee', 'status')
    search_fields = ['project', 'epic', 'title', 'assignee', 'status']
    list_per_page = 25

    def updated_date(self, obj):
        return format(obj.updated, 'Y-m-d')


admin.site.register(ProjectTask, ProjectTaskAdmin)