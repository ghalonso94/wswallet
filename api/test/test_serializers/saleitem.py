from datetime import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from api.serializer import SaleItemSerializer
from core.models import Sale, Company, Customer, SaleItem


class SaleItemSerializerTestCase(TestCase):

    user = User(username='test')
    company = Company(corporate_name='Company Test', registered_number='00.000.000/0000-00', user=user)
    customer = Customer(name='Test Customer', document='000.000.000-00')
    sale = Sale(customer=customer, company=company, number='123', sold_at=datetime.now())

    def setUp(self):
        self.sale_item = SaleItem(
            sale=self.sale, type='A', quantity=2.22, value=11.11
        )
        self.serializer = SaleItemSerializer(instance=self.sale_item)

    def test_verify_fields_serialized(self):
        """Verification test of SaleItem fields serializeds"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['created_at', 'updated_at', 'saleitem_id', 'sale', 'type', 'quantity', 'value']))

    def test_verify_content_fields_serialized(self):
        """Verification test of SaleItem content fields serializeds"""
        data = self.serializer.data
        self.assertEqual(data['saleitem_id'], str(self.sale_item.saleitem_id))
        self.assertEqual(data['sale'], self.sale_item.sale.sale_id)
        self.assertEqual(data['type'], self.sale_item.type)
        self.assertEqual(data['quantity'], str(self.sale_item.quantity))
        self.assertEqual(data['value'], str(self.sale_item.value))
