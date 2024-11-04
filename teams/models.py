from django.db import models
from django.contrib.auth.models import User


class ProjectTeam(models.Model):
    """A model for a team in a project."""
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='team_members')

    def __str__(self):
        member_names = ", ".join(
            [member.username for member in self.members.all()]
            )
        return f"{self.title} | Members: {member_names}"

    def is_user_member(self, user):
        return user in self.members.all()
