from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin',
            password='admin12345'
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username='user',
            password='userpwd',
            first_name='Fal',
            last_name='Gin',
            license_number='AAA12345'
        )

    def test_license_number_in_list(self):
        url = reverse("admin:taxi_driver_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)

    def test_license_number_in_detail_list(self):
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)
