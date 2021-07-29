import uuid

from django.db import models

# Create your models here.
from core.models import TimestampableMixin, Sale


class Cashback(TimestampableMixin, models.Model):
    cashback_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    value = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, null=False, blank=False)
    STATUS_CHOICES = (
        ('ACCEPTED', 'Accepted'),
        ('REFUSED', 'Refused'),
        ('PENDING', 'Pending'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=8, null=False, blank=False)

    class Meta:
        ordering = ['created_at']
