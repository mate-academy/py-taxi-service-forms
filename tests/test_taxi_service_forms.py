from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer


class CarTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            license_number="ADM12345",
            first_name="Admin",
            last_name="User",
            password="1qazcde3"
        )
        self.client.force_login(self.user)
        self.manufacturer = Manufacturer.objects.create(
            name="Lincoln",
            country="USA",
        )

    def create_car(self):
        return self.client.post(
            reverse("taxi:car-create"),
            {
                "model": "Continental",
                "manufacturer": 1,
                "drivers": [1]
            }
        )

    def test_create_car(self):
        response = self.create_car()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.get(id=1).model, "Continental")

    def test_update_car(self):
        self.create_car()
        response = self.client.post(
            reverse(
                "taxi:car-update",
                kwargs={"pk": 1}),
            {
                "pk": 1,
                "model": "Not Continental",
                "manufacturer": 1,
                "drivers": [1]
            }
        )
        Car.objects.get(id=1).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.get(id=1).model, "Not Continental")

    def test_delete_car(self):
        self.create_car()
        response = self.client.post(
            reverse("taxi:car-delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Car.objects.filter(id=1).exists())


class ManufacturerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            license_number="ADM12345",
            first_name="Admin",
            last_name="User",
            password="1qazcde3"
        )
        self.client.force_login(self.user)

    def create_manufacturer(self):
        return self.client.post(
            reverse(
                "taxi:manufacturer-create",
            ),
            {
                "name": "Lincoln",
                "country": "USA"
            }
        )

    def test_create_manufacturer(self):
        response = self.create_manufacturer()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Manufacturer.objects.get(id=1).name, "Lincoln")

    def test_update_manufacturer(self):
        self.create_manufacturer()
        response = self.client.post(
            reverse(
                "taxi:manufacturer-update",
                kwargs={"pk": 1}
            ),
            {
                "name": "Not Lincoln",
                "country": "USA"
            }
        )
        Manufacturer.objects.get(id=1).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Manufacturer.objects.get(id=1).name, "Not Lincoln")

    def test_delete_manufacturer(self):
        self.create_manufacturer()
        response = self.client.post(
            reverse("taxi:manufacturer-delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Manufacturer.objects.filter(id=1).exists())
