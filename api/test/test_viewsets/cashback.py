import json

from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

from core.models import Company


class CashbackViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cashback-list')
        self.user = User.objects.create_superuser('xpto', password='xpto')
        self.user.save()
        self.company = Company.objects.create(corporate_name='Company Test', registered_number='00.000.000/0000-00', user=self.user)
        self.company.save()

    def test_get_request_with_authenticated_user(self):
        """Verification test of get request to user authenticated"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request_with_authenticated_user(self):
        """Verification test of post request to user authenticated"""
        self.client.force_authenticate(self.user)
        data = {
            "sold_at": "2026-01-02 00:00:00",
            "customer": {
                "document": "663.663.710-24",
                "name": "JOSE DA SILVA",
            },
            "total": 100.00,
            "products": [
                {
                    "type": "A",
                    "value": 10.00,
                    "qty": 1,
                },
                {
                    "type": "B",
                    "value": 10.00,
                    "qty": 9,
                }
            ],
        }
        response = self.client.post(self.list_url, data=json.dumps(data), content_type='application/json')
        self.company.delete()
        self.user.delete()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_post_request_with_invalid_document(self):
        """Verification test of post request to user authenticated"""
        self.client.force_authenticate(self.user)
        data = {
            "sold_at": "2026-01-02 00:00:00",
            "customer": {
                "document": "123.456.789-10",
                "name": "JOSE DA SILVA",
            },
            "total": 100.00,
            "products": [
                {
                    "type": "A",
                    "value": 10.00,
                    "qty": 1,
                },
                {
                    "type": "B",
                    "value": 10.00,
                    "qty": 9,
                }
            ],
        }
        response = self.client.post(self.list_url, data=json.dumps(data), content_type='application/json')
        self.company.delete()
        self.user.delete()
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_post_request_with_invalid_type(self):
        """Verification test of post request to user authenticated"""
        self.client.force_authenticate(self.user)
        data = {
            "sold_at": "2026-01-02 00:00:00",
            "customer": {
                "document": "123.456.789-10",
                "name": "JOSE DA SILVA",
            },
            "total": 100.00,
            "products": [
                {
                    "type": "D",
                    "value": 10.00,
                    "qty": 1,
                },
                {
                    "type": "B",
                    "value": 10.00,
                    "qty": 9,
                }
            ],
        }
        response = self.client.post(self.list_url, data=json.dumps(data), content_type='application/json')
        self.company.delete()
        self.user.delete()
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)


    def test_post_request_with_invalid_total(self):
        """Verification test of post request to user authenticated"""
        self.client.force_authenticate(self.user)
        data = {
            "sold_at": "2026-01-02 00:00:00",
            "customer": {
                "document": "123.456.789-10",
                "name": "JOSE DA SILVA",
            },
            "total": 99.99,
            "products": [
                {
                    "type": "D",
                    "value": 10.00,
                    "qty": 1,
                },
                {
                    "type": "B",
                    "value": 10.00,
                    "qty": 9,
                }
            ],
        }
        response = self.client.post(self.list_url, data=json.dumps(data), content_type='application/json')
        self.company.delete()
        self.user.delete()
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_post_request_with_invalid_date(self):
        """Verification test of post request to user authenticated"""
        self.client.force_authenticate(self.user)
        data = {
            "sold_at": "2026-01-32 00:00:00",
            "customer": {
                "document": "123.456.789-10",
                "name": "JOSE DA SILVA",
            },
            "total": 100.00,
            "products": [
                {
                    "type": "A",
                    "value": 10.00,
                    "qty": 1,
                },
                {
                    "type": "B",
                    "value": 10.00,
                    "qty": 9,
                }
            ],
        }
        response = self.client.post(self.list_url, data=json.dumps(data), content_type='application/json')
        self.company.delete()
        self.user.delete()
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)