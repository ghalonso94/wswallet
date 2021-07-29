import uuid

from django.db import models

# Create your models here.
from core.models import TimestampableMixin, Client, Company


class Sale(TimestampableMixin, models.Model):
    sale_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=10, null=True, blank=True, default=None)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sold_at = models.DateTimeField(null=False)

    class Meta:
        ordering = ['sold_at']
