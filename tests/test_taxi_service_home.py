import os

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer

TestCase.fixtures = ["taxi_service_db_data.json", ]


class HomePageTests(TestCase):
    def test_index_count_content_correctly(self):
        response = self.client.get(reverse("taxi:index"))
        num_drivers = get_user_model().objects.count()
        num_cars = Car.objects.count()
        num_manufacturers = Manufacturer.objects.count()

        self.assertContains(response, "Home page")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/index.html")
        self.assertEqual(response.context["num_drivers"], num_drivers)
        self.assertEqual(response.context["num_cars"], num_cars)
        self.assertEqual(
            response.context["num_manufacturers"],
            num_manufacturers
        )


class IsStylesCSSExistTests(TestCase):
    def test_styles_exist(self):
        file_exists = os.path.exists('static/css/styles.css')

        self.assertTrue(file_exists)
