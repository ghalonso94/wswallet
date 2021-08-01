from django.contrib.auth.models import User
from django.test import TestCase

from api.serializer import CompanySerializer
from core.models import Company


class CompanySerializerTestCase(TestCase):
    user = User(username='test')

    def setUp(self):
        self.company = Company(
            corporate_name='Company Test', registered_number='00.000.000/0000-00', user=self.user
        )
        self.serializer = CompanySerializer(instance=self.company)

    def test_verify_fields_serialized(self):
        """Verification test of Company fields serializeds"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         set(['created_at', 'updated_at', 'company_id', 'corporate_name', 'registered_number', 'user']))

    def test_verify_content_fields_serialized(self):
        """Verification test of Company content fields serializeds"""
        data = self.serializer.data
        self.assertEqual(data['company_id'], str(self.company.company_id))
        self.assertEqual(data['corporate_name'], self.company.corporate_name)
        self.assertEqual(data['registered_number'], self.company.registered_number)
        self.assertEqual(data['user'], None)

