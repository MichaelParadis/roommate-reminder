from django.db import models

TASK_STATUSES = [
    ('done', 'Done'),
    ('in-progress', 'In Progress'),
    ('todo', 'Todo')
]

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=256)
    deadline = models.DateField(null=True)
    is_important = models.BooleanField(default=False)
    status = models.CharField(choices=TASK_STATUSES, max_length=20, default='todo')
