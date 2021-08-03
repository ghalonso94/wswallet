import json

from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class CompanyViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Company-list')
        self.user = User.objects.create_superuser('root', password='root')

    def test_post_request_with_authenticated_user(self):
        """Verification test of get request to user authenticated"""
        self.client.force_authenticate(self.user)
        data = {
            'corporate_name': 'Company Test',
            'registered_number': '00.000.000/0000-00',
            'user': str(self.user.id)
        }
        response = self.client.post(self.list_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)