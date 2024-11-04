from django.db import models
from django.contrib.auth.models import User

TASK_STATUS = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]

class ProjectTask(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    epic = models.ForeignKey('epics.ProjectEpic', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=TASK_STATUS, default='todo')
    assignee = models.ForeignKey('teams.ProjectTeam', on_delete=models.CASCADE, blank=True, null=True, related_name="task_assignee")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the task."""
        return f"{self.title} located in {self.project.title} assigned to {self.epic.title} with team member {self.assignee} and status {self.status}"
