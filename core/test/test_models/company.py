from django.contrib.auth.models import User
from django.test import TestCase
from core.models import *

class CompanyModelTestCase(TestCase):

    user = User(username='test')

    def setUp(self):
        self.company = Company(
            corporate_name='Company Test',
            registered_number='00.000.000/0001-00',
            user=self.user
        )

    def test_verify_attrs_company(self):
        """Verification test of Company attributes"""
        self.assertEqual(self.company.corporate_name, 'Company Test')
        self.assertEqual(self.company.registered_number, '00.000.000/0001-00')
        self.assertEqual(self.company.user, self.user)
