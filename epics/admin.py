from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ProjectEpic

# Register your models here.

class ProjectEpicAdmin(SummernoteModelAdmin):
    list_display = ('title', 'project', 'start_date', 'end_date', 'created_on', 'updated_on')
    list_filter = ('title',)
    search_fields = ['project', 'title']
    list_per_page = 25


admin.site.register(ProjectEpic, ProjectEpicAdmin)
