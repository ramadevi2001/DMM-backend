from django.db import models

# Create your models here.

import uuid
from goals.models import Goal

class MonthlyGoal(models.Model):
    class MonthlyGoalStatus(models.TextChoices):
        TO_DO = 'To do', 'To do'
        IN_PROGRESS = 'In progress', 'In progress'
        DONE = 'Done', 'Done'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='monthly_goals')
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=False)
    target_date = models.DateTimeField(null=False)
    status = models.CharField(
        max_length=11,
        choices=MonthlyGoalStatus.choices,
        default=MonthlyGoalStatus.TO_DO,
    )

    def __str__(self):
        return self.title

