from rest_framework import viewsets
from core.models import Sale
from api.serializer import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):

    # Show all clients
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer