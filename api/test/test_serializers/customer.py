from django.test import TestCase

from api.serializer import CustomerSerializer
from core.models import Customer


class CustomerSerializerTestCase(TestCase):

    def setUp(self):
        self.customer = Customer(
            name='Company Test', document='00.000.000/0000-00'
        )
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_verify_fields_serialized(self):
        """Verification test of Customer fields serializeds"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         set(['created_at', 'updated_at', 'customer_id', 'name', 'document']))

    def test_verify_content_fields_serialized(self):
        """Verification test of Customer content fields serializeds"""
        data = self.serializer.data
        self.assertEqual(data['customer_id'], str(self.customer.customer_id))
        self.assertEqual(data['name'], self.customer.name)
        self.assertEqual(data['document'], self.customer.document)

