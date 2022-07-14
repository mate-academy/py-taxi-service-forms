from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Car, Manufacturer


class ModelsTest(TestCase):
    def test_driver_str(self):
        data = get_user_model().objects.create(
            username="user",
            first_name="test",
            last_name="user",
            licence_number=12345678
        )

        self.assertEqual(str(data), "user (test user)")
        self.assertEqual(data.licence_number, 12345678)


    def test_manufacturer_str(self):
        data = Manufacturer.objects.create(
            name="test_name",
            country="test_country"
        )

        self.assertEqual(str(data), "test_name test_country")
