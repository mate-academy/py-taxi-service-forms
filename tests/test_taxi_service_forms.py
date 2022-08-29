from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer

TestCase.fixtures = ["taxi_service_db_data.json", ]


class CarTest(TestCase):
    def setUp(self) -> None:
        self.client.force_login(get_user_model().objects.get(id=1))

    def test_update_car(self):
        response = self.client.post(
            reverse(
                "taxi:car-update",
                kwargs={"pk": 1}),
            {
                "pk": 1,
                "model": "Not Lincoln",
                "manufacturer": 3,
                "drivers": [2]
            }
        )
        Car.objects.get(id=1).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.get(id=1).model, "Not Lincoln")

    def test_create_car(self):
        response = self.client.post(
            reverse("taxi:car-create"),
            {
                "model": "Not only Lincoln",
                "manufacturer": 3,
                "drivers": [
                    2
                ]
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.get(id=8).model, "Not only Lincoln")

    def test_delete_car(self):
        response = self.client.post(
            reverse("taxi:car-delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Car.objects.filter(id=1).exists())


class ManufacturerTest(TestCase):
    def setUp(self) -> None:
        self.client.force_login(get_user_model().objects.get(id=1))

    def test_update_manufacturer(self):
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

    def test_create_manufacturer(self):
        response = self.client.post(
            reverse(
                "taxi:manufacturer-create",
            ),
            {
                "name": "Not Lincoln",
                "country": "USA"
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Manufacturer.objects.get(id=7).name, "Not Lincoln")

    def test_delete_car(self):
        response = self.client.post(
            reverse("taxi:manufacturer-delete", kwargs={"pk": 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Manufacturer.objects.filter(id=1).exists())
