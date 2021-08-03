import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.models import Sale, Company
from api.serializer import SaleSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SaleViewSet(viewsets.ModelViewSet):

    # Show all Customers
    serializer_class = SaleSerializer
    http_method_names = ['get', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """ Method for listing all sales """
        if request.user.is_staff:
            queryset = Sale.objects.all()
        else:
            queryset = Sale.objects.filter(company__user__exact=request.user)

        serializer = SaleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """ Method to recover a single sale """
        if request.user.is_staff:
            queryset = Sale.objects.all()
        else:
            queryset = Sale.objects.filter(company__user__exact=request.user)

        cashback = get_object_or_404(queryset, pk=pk)
        serializer = SaleSerializer(cashback)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """ Method to destroy a single sale """
        sale = get_object_or_404(Sale, pk=pk)
        if request.user.is_staff:
            sale.delete()
            return HttpResponse(json.dumps({'detail': 'Successful deleting object'}), status=status.HTTP_204_NO_CONTENT, content_type='application/json')
        else:
            company = Company.objects.filter(user=request.user).first()
            if sale.company == company:
                sale.delete()
                return HttpResponse(json.dumps({'detail': 'Successful deleting object'}), status=status.HTTP_204_NO_CONTENT, content_type='application/json')
            else:
                return HttpResponse(json.dumps({'detail': 'Not found'}), status=status.HTTP_406_NOT_ACCEPTABLE, content_type='application/json')


