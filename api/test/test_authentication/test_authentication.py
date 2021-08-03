from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Company-list')
        self.user = User.objects.create_superuser('root', password='root')

    def test_authentication_user_credentials(self):
        """User credentials verification test"""
        user = authenticate(username='root', password='root')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_get_request_with_not_authenticated_user(self):
        """Verification test of get request to user without authentication"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_incorrect_username(self):
        """Incorrect username verification test"""
        user = authenticate(username='rot', password='root')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_incorrect_password(self):
        """Incorrect password verification test"""
        user = authenticate(username='root', password='123')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_request_with_authenticated_user(self):
        """Verification test of get request to user authenticated"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)