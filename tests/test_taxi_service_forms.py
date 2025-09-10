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
            password="1qazcde3",
        )
        self.client.force_login(self.user)
        self.manufacturer = Manufacturer.objects.create(
            name="Lincoln",
            country="USA",
        )

    def test_create_car(self):
        response = self.client.post(
            reverse("taxi:car-create"),
            {
                "model": "Continental",
                "manufacturer": self.manufacturer.id,
                "drivers": [self.user.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Car.objects.get(id=self.user.cars.first().id).model, "Continental"
        )

    def test_update_car(self):
        car = Car.objects.create(
            model="Continental",
            manufacturer=self.manufacturer,
        )
        response = self.client.post(
            reverse("taxi:car-update", kwargs={"pk": car.id}),
            {
                "pk": car.id,
                "model": "Not Continental",
                "manufacturer": self.manufacturer.id,
                "drivers": [self.user.id],
            },
        )
        Car.objects.get(id=car.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.get(id=car.id).model, "Not Continental")

    def test_delete_car(self):
        car = Car.objects.create(
            model="Continental",
            manufacturer=self.manufacturer,
        )
        response = self.client.post(
            reverse("taxi:car-delete", kwargs={"pk": car.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Car.objects.filter(id=car.id).exists())


class ManufacturerTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            license_number="ADM12345",
            first_name="Admin",
            last_name="User",
            password="1qazcde3",
        )
        self.client.force_login(self.user)

    def test_create_manufacturer(self):
        response = self.client.post(
            reverse(
                "taxi:manufacturer-create",
            ),
            {"name": "Lincoln", "country": "USA"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Manufacturer.objects.get(id=1).name, "Lincoln")

    def test_update_manufacturer(self):
        manufacturer = Manufacturer.objects.create(
            name="Lincoln",
            country="USA",
        )
        response = self.client.post(
            reverse(
                "taxi:manufacturer-update", kwargs={"pk": manufacturer.id}
            ),
            {"name": "Not Lincoln", "country": "USA"},
        )
        Manufacturer.objects.get(id=manufacturer.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Manufacturer.objects.get(id=manufacturer.id).name, "Not Lincoln"
        )

    def test_delete_manufacturer(self):
        manufacturer = Manufacturer.objects.create(
            name="Lincoln",
            country="USA",
        )
        response = self.client.post(
            reverse("taxi:manufacturer-delete", kwargs={"pk": manufacturer.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Manufacturer.objects.filter(id=manufacturer.id).exists()
        )
