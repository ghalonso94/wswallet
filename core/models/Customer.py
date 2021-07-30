import uuid

from cpf_field.models import CPFField
from django.db import models

# Create your models here.
from core.models import TimestampableMixin


class Customer(TimestampableMixin, models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True, default='')
    document = CPFField(max_length=18, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} | {self.document}'
