from django.db import models
from django.contrib.auth.models import User
from django.db.models import Prefetch

# Create your models here.


class ProjectTeam(models.Model):
    """A model for a team in a project."""
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='team_members')

    def __str__(self):
        """Return a string representation of the team."""
        return f"{self.title} - {self.project.id}. {self.project.title} with {self.members.count()} members"

