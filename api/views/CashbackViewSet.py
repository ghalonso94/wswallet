import json

from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Cashback, Sale, Customer, SaleItem, Company
from api.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):

    # Show all Customers
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

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
            customer = Customer(name=name, document=document)
            customer.save()

        # Atribui o consumidor à venda e salva
        sale.customer = customer
        sale.save()

        total = request.data["total"]

        sale_item_list = []

        # Obtendo lista de produtos e salvando amarrados à venda instanciada
        for p in request.data["products"]:
            sale_item = SaleItem(sale=sale)
            sale_item.type = p["type"]
            sale_item.value = p["value"]
            sale_item.quantity = p["qty"]
            sale_item.save()
            sale_item_list.append(sale_item)

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

        return HttpResponse({json.dumps(sale)}, status=status.HTTP_201_CREATED, content_type='application/json')