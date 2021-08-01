from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from core.models import *


class SaleModelTestCase(TestCase):

    user = User(username='test')
    company = Company(corporate_name='Company Test', registered_number='00.000.000/0000-00', user=user)
    customer = Customer(name='Customer Test', document='000.000.000-00')

    def setUp(self):
        self.sale = Sale(
            number='123', company=self.company, customer=self.customer, sold_at=datetime.now()
        )

    def test_verify_attrs_sale(self):
        """Verification test of Sale attributes"""
        self.assertEqual(self.sale.number, '123')
        self.assertEqual(self.sale.company, self.company)
        self.assertEqual(self.sale.customer, self.customer)
        self.assertEqual(self.sale.sold_at, datetime.now())
