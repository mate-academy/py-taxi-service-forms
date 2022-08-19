from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import os.path

from taxi.models import Car, Manufacturer, Driver

TestCase.fixtures = ['taxi_service_db_data.json', ]


class PublicTests(TestCase):
    def test_index_login_required(self):
        response = self.client.get(reverse("taxi:index"))

        self.assertNotEqual(response.status_code, 200)
