import json

from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class CustomerViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Customer-list')
        self.user = User.objects.create_superuser('root', password='root')

    def test_get_request_with_authenticated_user(self):
        """Verification test of get request to user authenticated"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)