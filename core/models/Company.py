import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from core.models import TimestampableMixin


class Company(TimestampableMixin, models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    corporate_name = models.CharField(max_length=150, null=True, blank=True, default='')
    registered_number = models.CharField(max_length=18, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.corporate_name} | {self.registered_number}'