from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('root', password='root')

    def test_authentication_user_credentials(self):
        """User credentials verification test"""
        user = authenticate(username='root', password='root')
        self.assertTrue((user is not None) and user.is_authenticated)