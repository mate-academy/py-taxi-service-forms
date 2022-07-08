from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class TestModels(TestCase):

    def test_str_manufacturer(self):
        manufacturer = Manufacturer.objects.create(name="Tesla", country="USA")

        self.assertEqual(str(manufacturer),
                         f"{manufacturer.name} {manufacturer.country}")

    def test_str_driver(self):
        driver = get_user_model().objects.create_user(username="test_username",
                                                      first_name="Name",
                                                      last_name="Surname",
                                                      password="test1234")

        self.assertEqual(str(driver),
                         f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_str_car(self):
        manufacturer = Manufacturer.objects.create(name="Tesla",
                                                   country="USA")
        car = Car.objects.create(model="Model S",
                                 manufacturer=manufacturer)

        self.assertEqual(str(car), car.model)

    def test_license_number_for_driver(self):
        username = "test_username"
        first_name = "Name"
        last_name = "Surname"
        password = "test1234"
        license_number = "QWE12345"
        driver = get_user_model().objects.create_user(username=username,
                                                      first_name=first_name,
                                                      last_name=last_name,
                                                      password=password,
                                                      license_number=license_number)

        self.assertEqual(driver.username, username)
        self.assertEqual(driver.first_name, first_name)
        self.assertEqual(driver.last_name, last_name)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)
