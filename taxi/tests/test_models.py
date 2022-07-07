from django.test import TestCase

from taxi.models import Driver, Car, Manufacturer


class ModelsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Driver.objects.create(first_name='Big', last_name='Bob')

    def test_driver_first_name_label(self):
        driver = Driver.objects.get(id=1)
        field_label = driver._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_driver_first_name_max_length(self):
        driver = Driver.objects.get(id=1)
        max_length = driver._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 150)

    def test_driver_license_number(self):
        driver = Driver.objects.create_user(
            username='test1',
            password='pwd12345',
            license_number='AAAAaaaa!'
        )

        self.assertEquals(driver.username, 'test1')
        self.assertTrue(driver.check_password('pwd12345')),
        self.assertNotEquals(driver.license_number, 'BBBBbbbb?')

    def test_driver_str_method(self):
        driver = Driver.objects.get(id=1)
        expected_object_name = f' ({driver.first_name} {driver.last_name})'
        self.assertEquals(expected_object_name, str(driver))

    def test_car_str_method(self):
        manufacturer = Manufacturer.objects.create(name='Toyota', country='Japan')
        car = Car.objects.create(model='Bentley', manufacturer=manufacturer)
        self.assertEquals(str(car), 'Bentley')

    def test_manufacturer_str_method(self):
        manufacturer = Manufacturer.objects.create(name='Toyota', country='Japan')
        self.assertNotEquals(str(manufacturer), "Wrong output")
