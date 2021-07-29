from rest_framework import viewsets
from core.models import SaleItem
from api.serializer import SaleItemSerializer


class SaleItemViewSet(viewsets.ModelViewSet):

    # Show all clients
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer