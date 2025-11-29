from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Restaurant
# Create your tests here.
class RestaurantInfoAPITestCase(APITestCase):
    def setUp(self):
        self.restaurant=Restaurant.objects.create(name="Test Restaurant")

    def test_get_restaurant_info(self):
        url=f'/api/restaurant-info/{self.restaurant.id}/'
        response=self.client.get(url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['name'],'Test Restaurant')
