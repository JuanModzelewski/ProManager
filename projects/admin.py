from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['title', 'description']
    list_per_page = 25
    summernote_fields = ('description',)

admin.site.register(Project, ProjectAdmin)