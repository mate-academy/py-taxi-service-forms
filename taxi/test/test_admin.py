from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestAdmin(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="1234admin"
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="driver",
            password="1234qwer",
            license_number="QWE12345",
            first_name="test",
            last_name="last"
        )

    def test_driver_license_listed(self):

        url = reverse("admin:taxi_driver_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)

    def test_driver_detail_license_listed(self):

        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)
