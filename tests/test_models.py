from django.test import TestCase
from restaurant.models import menu

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import menuSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class menuItemTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
