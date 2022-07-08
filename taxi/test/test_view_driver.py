from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer, Driver

DRIVER_LIST_URL = reverse("taxi:driver-list")
REDIRECT_URL_USER_NOT_LOGIN = "/accounts/login/?next=/drivers/"


class PublicDriversListTest(TestCase):
    def setUp(self):
        self.res = self.client.get(DRIVER_LIST_URL)

    def test_login_require(self):
        self.assertNotEqual(self.res.status_code, 200)
        self.assertRedirects(self.res, REDIRECT_URL_USER_NOT_LOGIN)


class PrivateDriversListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="1234qwer"
        )
        self.client.force_login(self.user)

        self.driver = get_user_model().objects.create_user(
            username="driver",
            password="1234qwer",
            license_number="QWE12345",
            first_name="test",
            last_name="last"
        )

    def test_retrieve_drivers(self):

        response = self.client.get(DRIVER_LIST_URL)
        drivers = Driver.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["driver_list"]), list(drivers))
        self.assertTemplateUsed(response, "taxi/driver_list.html")

    def test_open_driver_detail_view(self):
        url = reverse("taxi:driver-detail", args=(self.driver.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_driver_create_view(self):
        url = reverse("taxi:driver_create")
        response = self.client.post(url)

        self.assertEqual(response.status_code, 200)

    def test_driver_update_view(self):
        new_license = {"license_number": "ZXC12345"}
        url = reverse("taxi:driver_update", args=[self.driver.id,])
        response = self.client.post(path=url, data=new_license)
        update_driver = get_user_model().objects.get(id=self.driver.id)

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(update_driver.license_number, new_license["license_number"])
