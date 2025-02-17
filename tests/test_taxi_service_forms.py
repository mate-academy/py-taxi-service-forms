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
        """Test car creation and driver association"""
        response = self.client.post(
            reverse("taxi:car-create"),
            {
                "model": "Continental",
                "manufacturer": self.manufacturer.id,
                "drivers": [self.user.id],
            },
            follow=True,  # Ensure it follows redirects
        )
        self.assertEqual(response.status_code, 200)  # Should land on success page
        self.assertEqual(Car.objects.count(), 1)
        car = Car.objects.first()
        self.assertEqual(car.model, "Continental")
        self.assertIn(self.user, car.drivers.all())  # Ensure driver is associated

    def test_update_car(self):
        """Test car update"""
        car = Car.objects.create(
            model="Continental",
            manufacturer=self.manufacturer,
        )
        car.drivers.add(self.user)  # Add driver to the car

        response = self.client.post(
            reverse("taxi:car-update", kwargs={"pk": car.id}),
            {
                "model": "Not Continental",
                "manufacturer": self.manufacturer.id,
                "drivers": [self.user.id],  # Keep driver assigned
            },
            follow=True,
        )

        car.refresh_from_db()  # Ensure we have the latest data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(car.model, "Not Continental")

    def test_delete_car(self):
        """Test car deletion"""
        car = Car.objects.create(
            model="Continental",
            manufacturer=self.manufacturer,
        )
        self.assertEqual(Car.objects.count(), 1)

        response = self.client.post(
            reverse("taxi:car-delete", kwargs={"pk": car.id}), follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Car.objects.count(), 0)  # Ensure car is deleted


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
        """Test manufacturer creation"""
        response = self.client.post(
            reverse("taxi:manufacturer-create"),
            {"name": "Lincoln", "country": "USA"},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Manufacturer.objects.count(), 1)
        manufacturer = Manufacturer.objects.first()
        self.assertEqual(manufacturer.name, "Lincoln")

    def test_update_manufacturer(self):
        """Test manufacturer update"""
        manufacturer = Manufacturer.objects.create(
            name="Lincoln",
            country="USA",
        )

        response = self.client.post(
            reverse("taxi:manufacturer-update", kwargs={"pk": manufacturer.id}),
            {"name": "Not Lincoln", "country": "USA"},
            follow=True,
        )

        manufacturer.refresh_from_db()  # Ensure we have the latest changes
        self.assertEqual(response.status_code, 200)
        self.assertEqual(manufacturer.name, "Not Lincoln")

    def test_delete_manufacturer(self):
        """Test manufacturer deletion"""
        manufacturer = Manufacturer.objects.create(
            name="Lincoln",
            country="USA",
        )
        self.assertEqual(Manufacturer.objects.count(), 1)

        response = self.client.post(
            reverse("taxi:manufacturer-delete", kwargs={"pk": manufacturer.id}),
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Manufacturer.objects.count(), 0)  # Ensure manufacturer is deleted
