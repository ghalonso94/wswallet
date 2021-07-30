from rest_framework import viewsets
from core.models import Sale
from api.serializer import SaleSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SaleViewSet(viewsets.ModelViewSet):

    # Show all Customers
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]