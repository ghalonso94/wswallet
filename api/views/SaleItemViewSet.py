from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.models import SaleItem
from api.serializer import SaleItemSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SaleItemViewSet(viewsets.ModelViewSet):

    # Show all Customers
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    http_method_names = ['get']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """ Method for listing all sale items """
        if request.user.is_staff:
            queryset = SaleItem.objects.all()
        else:
            queryset = SaleItem.objects.filter(sale__company__user__exact=request.user)

        serializer = SaleItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """ Method to recover a single sale item """
        if request.user.is_staff:
            queryset = SaleItem.objects.all()
        else:
            queryset = SaleItem.objects.filter(sale__company__user__exact=request.user)

        cashback = get_object_or_404(queryset, pk=pk)
        serializer = SaleItemSerializer(cashback)
        return Response(serializer.data)