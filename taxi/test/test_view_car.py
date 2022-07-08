from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Manufacturer

CARS_LIST_URL = reverse("taxi:car-list")
CAR_DETAIL_URL = "taxi:car-detail"
REDIRECT_URL_USER_NOT_LOGIN = "/accounts/login/?next=/cars/"


class PublicCarsListTest(TestCase):
    def setUp(self):
        self.res = self.client.get(CARS_LIST_URL)

    def test_login_require(self):
        self.assertNotEqual(self.res.status_code, 200)
        self.assertRedirects(self.res, REDIRECT_URL_USER_NOT_LOGIN)


class PrivateCarsListTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="1234qwer"
        )
        self.client.force_login(self.user)

    def test_retrieve_cars(self):
        manufacturer = Manufacturer.objects.create(name="tesTm", country="Ua")
        Car.objects.create(model="test1", manufacturer=manufacturer)
        Car.objects.create(model="test2", manufacturer=manufacturer)

        response = self.client.get(CARS_LIST_URL)
        cars = Car.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["car_list"]), list(cars))
        self.assertTemplateUsed(response, "taxi/car_list.html")

    def test_open_car_detail_view(self):
        manufacturer = Manufacturer.objects.create(name="tesTm", country="Ua")
        car = Car.objects.create(model="test1", manufacturer=manufacturer)
        url = reverse(CAR_DETAIL_URL, args=(car.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
