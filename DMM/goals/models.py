# goals/models.py
from django.db import models
from choices.models import Choice  # Import Choice model here
import uuid

class Goal(models.Model):
    class GoalStatus(models.TextChoices):
        TO_DO = 'To do', 'To do'
        IN_PROGRESS = 'In progress', 'In progress'
        DONE = 'Done', 'Done'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='goals')
    goal = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=False)
    target_date = models.DateTimeField(null=False)
    status = models.CharField(
        max_length=11,
        choices=GoalStatus.choices,
        default=GoalStatus.TO_DO,
    )

    def __str__(self):
        return self.goal
