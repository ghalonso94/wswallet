import uuid

from django.db import models

# Create your models here.
from core.models import TimestampableMixin


class Client(TimestampableMixin, models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True, default='')
    document = models.CharField(max_length=18, null=False, blank=False)

    class Meta:
        ordering = ['created_at']
