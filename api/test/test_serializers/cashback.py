
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from api.serializer import CashbackSerializer
from core.models import Cashback, Sale, Company, Customer



class CashbackSerializerTestCase(TestCase):

    user = User(username='test')
    customer = Customer(name='Test Customer', document='000.000.000-00')

    def setUp(self):
        self.cashback = Cashback(
            status='PENDING', value='2.00', sale=Sale(sold_at=datetime.now())
        )
        self.serializer = CashbackSerializer(instance=self.cashback)

    def test_verify_fields_serialized(self):
        """Verification test of Cashback fields serializeds"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['created_at', 'updated_at', 'cashback_id', 'status', 'value', 'sale']))

    def test_verify_content_fields_serialized(self):
        """Verification test of Cashback content fields serializeds"""
        data = self.serializer.data
        self.assertEqual(data['status'], self.cashback.status)
        self.assertEqual(data['value'], self.cashback.value)
        self.assertEqual(data['sale'], self.cashback.sale.sale_id)
