import uuid

from django.db import models

# Create your models here.
from core.models import TimestampableMixin


class Company(TimestampableMixin, models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    corporate_name = models.CharField(max_length=150, null=True, blank=True, default='')
    registered_number = models.CharField(max_length=18, null=False, blank=False)

    class Meta:
        ordering = ['created_at']