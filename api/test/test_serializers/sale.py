
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from api.serializer import SaleSerializer
from core.models import Sale, Company, Customer



class SaleSerializerTestCase(TestCase):

    user = User(username='test')
    company = Company(corporate_name='Company Test', registered_number='00.000.000/0000-00', user=user)
    customer = Customer(name='Test Customer', document='000.000.000-00')

    def setUp(self):
        self.sale = Sale(
            number='123', company=self.company, customer=self.customer, sold_at=datetime.now()
        )
        self.serializer = SaleSerializer(instance=self.sale)

    def test_verify_fields_serialized(self):
        """Verification test of Sale fields serializeds"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['created_at', 'updated_at', 'sale_id', 'number', 'company', 'customer', 'sold_at']))

    def test_verify_content_fields_serialized(self):
        """Verification test of Sale content fields serializeds"""
        data = self.serializer.data
        self.assertEqual(data['sale_id'], str(self.sale.sale_id))
        self.assertEqual(data['number'], self.sale.number)
        self.assertEqual(data['company'], self.sale.company.company_id)
        self.assertEqual(data['customer'], self.sale.customer.customer_id)
        self.assertEqual(data['sold_at'], str(self.sale.sold_at).replace(' ','T'))
