from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate
from . import models, views
from django.urls import reverse
from django.contrib.auth.models import User

def get_auth_client():
    user_data = {"username": "testuser", "password": "fortesting"}
    client = APIClient()
    user_response = client.post('/api/auth/users/', user_data)
    jwt_response = client.post('/api/auth/jwt/create/', user_data)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                       jwt_response.data['access'])
    return client

class CountryTestCase(TestCase):

    def setUp(self):
        self.client = get_auth_client()
        self.url = reverse('account:countries')
        if models.Country.objects.count() != 0:
            models.Country.objects.clear()
    
    def test_api_get_all_countries(self):
        self.assertEqual(models.Country.objects.count(), 0)
        models.Country.objects.create(name='Japan')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Country.objects.count(), 1)
        models.Country.objects.create(name='USA')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Country.objects.count(), 2)
    
    def test_api_get_filtered_countries(self):
        self.assertEqual(models.Country.objects.count(), 0)
        models.Country.objects.create(name='Japan')
        models.Country.objects.create(name='USA')
        response = self.client.get('{}?starts-with=j'.format(self.url) )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
            

    def test_api_cannot_create_country(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    