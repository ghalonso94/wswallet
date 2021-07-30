from rest_framework import viewsets
from core.models import SaleItem
from api.serializer import SaleItemSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SaleItemViewSet(viewsets.ModelViewSet):

    # Show all Customers
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]