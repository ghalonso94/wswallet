import uuid

from django.db import models

# Create your models here.
from core.models import TimestampableMixin, Sale

class SaleItem(TimestampableMixin, models.Model):
    saleitem_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, null=False, blank=False)
    quantity = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, null=False, blank=False)
    value = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, null=False, blank=False)

    class Meta:
        ordering = ['created_at']