from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer

CAR_LIST_URL = reverse("taxi:car-list")
CAR_DETAIL_URL = reverse("taxi:car-detail", args=[1])
CAR_DELIT_URL = reverse("taxi:car-delete", args=[1])

class PublicCarListTests(TestCase):

    def test_access_to_car_list_no_authorised_users(self):
        response = self.client.get(CAR_LIST_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateCarTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "qwerty12345"
        )
        self.client.force_login(self.user)

    def test_car_str(self):
        data = Car.objects.create(
            model="test_car",
            manufacturer=Manufacturer.objects.create(
                name="test_name",
                country="test_country"
            )
        )

        self.assertEqual(str(data), "test_car")

    def test_access_to_car_list(self):
        Car.objects.create(
            model="test_car1",
            manufacturer=Manufacturer.objects.create(
                name="test_name1",
                country="test_country1"
            )
        )
        Car.objects.create(
            model="test_car2",
            manufacturer=Manufacturer.objects.create(
                name="test_name2",
                country="test_country2"
            )
        )

        response = self.client.get(CAR_LIST_URL)
        all_cars = Car.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["car_list"]), list(all_cars))
        self.assertTemplateUsed(response, "taxi/car_list.html")

    def test_access_to_car_detail(self):
        Car.objects.create(
            model="test_car1",
            manufacturer=Manufacturer.objects.create(
                name="test_name1",
                country="test_country1"
            )
        )
        detail_car_response = self.client.get(CAR_DETAIL_URL)
        self.assertEqual(detail_car_response.status_code, 200)
        self.assertTemplateUsed(detail_car_response, "taxi/car_detail.html")

    def test_access_to_car_delete(self):
        Car.objects.create(
            model="test_car1",
            manufacturer=Manufacturer.objects.create(
                name="test_name1",
                country="test_country1"
            )
        )
        delete_car_response = self.client.get(CAR_DELIT_URL)
        self.assertEqual(delete_car_response.status_code, 200)
        self.assertTemplateUsed(
            delete_car_response,
            "taxi/car_confirm_delete.html"
        )
