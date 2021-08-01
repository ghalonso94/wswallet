from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from core.models import *


class SaleItemModelTestCase(TestCase):

    user = User(username='test')
    company = Company(corporate_name='Company Test', registered_number='00.000.000/0000-00', user=user)
    customer = Customer(name='Customer Test', document='000.000.000-00')
    sale = Sale(number='123', company=company, customer=customer, sold_at=datetime.now())

    def setUp(self):
        self.sale_item = SaleItem(
            sale=self.sale, type='A', quantity='2.22', value='11.11'
        )

    def test_verify_attrs_sale_item(self):
        """Verification test of SaleItem attributes"""
        self.assertEqual(self.sale_item.sale, self.sale)
        self.assertEqual(self.sale_item.type, 'A')
        self.assertEqual(self.sale_item.quantity, '2.22')
        self.assertEqual(self.sale_item.value, '11.11')
