from django.test import TestCase
from core.models import *


class CustomerModelTestCase(TestCase):

    def setUp(self):
        self.customer = Customer(
            name='Customer Test',
            document='000.000.000-00',
        )

    def test_verify_attrs_company(self):
        """Verification test of company attributes"""
        self.assertEqual(self.customer.name, 'Customer Test')
        self.assertEqual(self.customer.document, '000.000.000-00')
