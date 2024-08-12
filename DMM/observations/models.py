from django.db import models
import uuid
from django.conf import settings

class Observation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='observations')
    observation = models.TextField()
    action_plan = models.JSONField()

    class Meta:
        unique_together = ('user', 'observation')

    def __str__(self):
        return f'Observation by {self.user.email}'
