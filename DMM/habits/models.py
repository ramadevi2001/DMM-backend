from django.db import models
import uuid
from django.conf import settings
from monthly_goals.models import MonthlyGoal

class Habit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    monthly_goal = models.ForeignKey(MonthlyGoal, on_delete=models.CASCADE, related_name='habits_monthlygoal')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    planned_period_minutes = models.PositiveIntegerField(null=False)
    location = models.CharField(max_length=255, null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    productivity = models.FloatField(null=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
