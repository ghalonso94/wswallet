from rest_framework import viewsets
from core.models import Customer
from api.serializer import CustomerSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):

    # Show all Customers
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]