from django.db import models


from user.models import User
# Create your models here.
import uuid


class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    become = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='choices_user')

    class Meta:
        unique_together = ('become', 'user')
    def __str__(self):
        return self.become


