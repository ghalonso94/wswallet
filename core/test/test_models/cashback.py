from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from core.models import *


class CashbackModelTestCase(TestCase):

    user = User(username='test')
    company = Company(corporate_name='Company Test', registered_number='00.000.000/0000-00', user=user)
    customer = Customer(name='Customer Test', document='000.000.000-00')
    sale = Sale(number='123', company=company, customer=customer, sold_at=datetime.now())

    def setUp(self):
        self.cashback = Cashback(
            sale=self.sale, value='10.00', status='ACCEPTED'
        )

    def test_verify_attrs_cashback(self):
        """Verification test of Cashback attributes"""
        self.assertEqual(self.cashback.sale, self.sale)
        self.assertEqual(self.cashback.value, '10.00')
        self.assertEqual(self.cashback.status, 'ACCEPTED')
