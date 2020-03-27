from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

status_choices = (
    ("NEW", "New"),
    ("IN_PROGRESS", "In Progress"),
    ("COMPLETED", "Completed"),
    ("ARCHIVED", "Archived"),
)


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=status_choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    task_creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    assigned_to = models.ManyToManyField(User, blank=True, related_name="assigned_to")


class Comment(models.Model):
    comment = models.CharField(max_length=220)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, null=True, related_name="commented_by", on_delete=models.SET_NULL)

