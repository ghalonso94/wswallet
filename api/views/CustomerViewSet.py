import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.models import Customer
from api.serializer import CustomerSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request):
        """ Method for listing all sales """
        if request.user.is_staff:
            queryset = Customer.objects.all()
        else:
            queryset = Customer.objects.filter(company__user__exact=request.user)

        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """ Method to recover a single sale """
        if request.user.is_staff:
            queryset = Customer.objects.all()
        else:
            queryset = Customer.objects.filter(company__user__exact=request.user)

        cashback = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(cashback)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """ Method to destroy a single customer
        
         @:param permission_required:is_staff (user must be from the staff)"""
        customer = get_object_or_404(Customer, pk=pk)
        if request.user.is_staff:
            customer.delete()
            return HttpResponse(json.dumps({'detail': 'Successful deleting object'}), status=status.HTTP_204_NO_CONTENT, content_type='application/json')
        else:

            return HttpResponse(json.dumps({'detail': 'Successful deleting object'}), status=status.HTTP_204_NO_CONTENT, content_type='application/json')
