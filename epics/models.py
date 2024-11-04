from django.db import models
from django.contrib.auth.models import User


class ProjectEpic(models.Model):
    """A model representing an epic in a project."""
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the epic."""
        return f"{self.title}"