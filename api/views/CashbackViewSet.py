import json
import requests

from datetime import datetime

from django.db import transaction
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from validate_docbr import CPF
from core.models import Cashback, Sale, Customer, SaleItem, Company
from api.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing or retrieving Cashbacks.
    """

    serializer_class = CashbackSerializer
    http_method_names = ['post', 'get', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """ Method for listing all Company cashbacks """
        if request.user.is_staff:
            queryset = Cashback.objects.all()
        else:
            queryset = Cashback.objects.filter(sale__company__user__exact=request.user)

        serializer = CashbackSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """ Method to recover a single Company cashback """
        if request.user.is_staff:
            queryset = Cashback.objects.all()
        else:
            queryset = Cashback.objects.filter(sale__company__user__exact=request.user)

        cashback = get_object_or_404(queryset, pk=pk)
        serializer = CashbackSerializer(cashback)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """ Method to create a new Company cashback """
        with transaction.atomic():

            try:
                datetime.strptime(request.data["sold_at"], '%Y-%m-%d %H:%M:%S')
            except Exception as ex:
                response = {
                    'error': 'Incorrect field "sold_at" format, should be YYYY-MM-DD 00:00:00'
                }
                return HttpResponse({json.dumps(response)}, status=status.HTTP_406_NOT_ACCEPTABLE, content_type='application/json')

            # Criando uma nova venda
            sale = Sale()
            sale.sold_at = request.data["sold_at"]
            sale.company = Company.objects.filter(user=request.user).first()

            # Tratando exceção para caso não envie o número da venda (não obrigatório)
            try:
                sale.number = request.data["number"]
            except:
                pass

            # Obtendo informações do consumidor
            document = request.data["customer"]["document"]
            name = request.data["customer"]["name"]

            # Limpando dados do documento
            document = str(document).replace('.','').replace('-','')

            # Verificando se consumidor já existe
            customer = Customer.objects.filter(document=document).first()

            # Se não encontrar nenhum consumidor, cria um novo
            if not customer:
                # Validando CPF
                cpf = CPF()
                try:
                    validation = cpf.validate(document)
                    if validation:
                        customer = Customer(name=name, document=document)
                        customer.save()
                    else:
                        response = {
                            'error': 'field "document" is invalid (CPF)'
                        }
                        return HttpResponse({json.dumps(response)}, status=status.HTTP_406_NOT_ACCEPTABLE, content_type='application/json')
                except Exception as ex:
                    response = {
                        'error': 'field "document" is invalid (CPF)'
                    }
                    return HttpResponse({json.dumps(response)}, status=status.HTTP_406_NOT_ACCEPTABLE, content_type='application/json')

            # Atribui o consumidor à venda e salva
            sale.customer = customer
            sale.save()

            cashback = Cashback(status='PENDING', sale=sale)

            total = request.data["total"]

            sale_item_list = []

            total_conference = 0.00

            validate = True
            # Validando todos os tipos de produtos
            for p in request.data["products"]:
                if not p["type"] in ['A', 'B', 'C']:
                    validate = False

            if not validate:
                sale.delete()
                response = {
                    'error': 'field "type" is invalid'
                }
                return HttpResponse({json.dumps(response)}, status=status.HTTP_406_NOT_ACCEPTABLE, content_type='application/json')
            else:
                # Obtendo lista de produtos e salvando amarrados à venda instanciada
                for p in request.data["products"]:
                    sale_item = SaleItem(sale=sale)
                    sale_item.type = p["type"]
                    sale_item.value = p["value"]
                    sale_item.quantity = p["qty"]
                    sale_item.save()
                    total_conference += float(sale_item.value)
                    sale_item_list.append(sale_item)

            #Conferindo se os valores batem com o total
            if float(total) != float(total_conference):
                response = {
                    'error': 'field "total" does not match the sum of the products'
                }
                return HttpResponse({json.dumps(response)}, status=status.HTTP_406_NOT_ACCEPTABLE, content_type='application/json')

            # Montando dict dos itens para retornar na API
            product_list = []
            for sale_item in sale_item_list:
                sale_item = {
                    'product_id': str(sale_item.saleitem_id),
                    'type': sale_item.type,
                    'qty': str(sale_item.quantity),
                    'value': str(sale_item.value)
                }
                product_list.append(sale_item)

            # Montando dict do consumidor para retorno
            customer = {
                'customer_id': str(customer.customer_id),
                'created_at': str(customer.created_at),
                'document': customer.document,
                'name': customer.name,
            }

            # Montando dict da venda total para retorno
            sale = {
                'sale_id': str(sale.sale_id),
                'created_at': str(sale.created_at),
                'sold_at': str(sale.sold_at),
                'total': str(total),
                'customer': customer,
                'product_list': product_list
            }

            # Calculando cashback
            cashback.value = (float(total) * 10)/100
            cashback.save()

            # Enviando cashback calculado para a API secundária
            url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'
            data = {
                'document': customer["document"],
                'cashback': cashback.value
            }

            response = requests.post(url, data = data)

            # Se o status de retorno for 201, muda o status do cashback para ACCEPTED
            if response.status_code == 201:
                cashback.status = 'ACCEPTED'
                cashback.save()

            cashback = {
                'created_at': str(cashback.created_at),
                'cashback_id': str(cashback.cashback_id),
                'response_status': str(response.status_code),
                'message': 'Cashback criado com sucesso!',
                'cashback_value': cashback.value,
                'sale': sale
            }

            return HttpResponse({json.dumps(cashback)}, status=status.HTTP_201_CREATED, content_type='application/json')