from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Driver, Car, Manufacturer

MANUFACTURER_LIST_URL = reverse("taxi:manufacturer_list")
DRIVER_LIST_URL = reverse("taxi:driver_list")
CAR_LIST_URL = reverse("taxi:car_list")


class ViewTests(TestCase):
    def setUp(self) -> None:
        self.driver1 = get_user_model().objects.create_user(
            username="joyce.byers",
            license_number="JOY26458",
            first_name="Joyce",
            last_name="Byers",
            password="1qazcde3"
        )
        self.driver2 = get_user_model().objects.create_user(
            username="jim.hopper",
            license_number="JIM26531",
            first_name="Jim",
            last_name="Hopper",
            password="2wsxvfr4"
        )

        self.manufacturer1 = Manufacturer.objects.create(
            name="Lincoln",
            country="USA"
        )
        self.manufacturer2 = Manufacturer.objects.create(
            name="General Motors",
            country="USA"
        )

        self.car1 = Car.objects.create(
            model="test_name_1",
            manufacturer=self.manufacturer1
        )
        self.car2 = Car.objects.create(
            model="Cadillac Escalade",
            manufacturer=self.manufacturer2
        )
        self.car1.drivers.add(self.driver1)
        self.car2.drivers.add(self.driver2)

    def test_manufacturer_list_response_and_display_correct_content(self):
        manufacturer_list = Manufacturer.objects.all()
        response = self.client.get(MANUFACTURER_LIST_URL)

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            list(response.context["manufacturer_list"]),
            list(manufacturer_list)
        )
        self.assertTemplateUsed(
            response,
            "taxi/manufacturer_list.html"
        )

    def test_manufacturer_list_has_pagination_and_sorted_by_name(self):
        self.manufacturer3 = Manufacturer.objects.create(
            name="Ford Motor Company",
            country="USA"
        )
        response = self.client.get(
            MANUFACTURER_LIST_URL,
            {"page": 2}
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            list(response.context["manufacturer_list"]),
            [self.manufacturer1]
        )

    def test_car_list_response_and_display_correct_content(self):
        car_list = Car.objects.all()
        response = self.client.get(CAR_LIST_URL)

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            list(response.context["car_list"]),
            list(car_list)
        )
        self.assertTemplateUsed(
            response,
            "taxi/car_list.html"
        )

    def test_car_list_has_pagination(self):
        self.manufacturer3 = Manufacturer.objects.create(
            name="Ford Motor Company",
            country="USA"
        )
        self.car3 = Car.objects.create(
            model="Lincoln Continental",
            manufacturer=self.manufacturer2
        )
        self.car3.drivers.add(self.driver1)

        response = self.client.get(
            CAR_LIST_URL,
            {"page": 2}
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_car_detail_response(self):
        response = self.client.get(reverse("taxi:car_detail", args=[self.car2.id]))

        self.assertEqual(
            response.status_code,
            200
        )

    def test_driver_list_response_and_display_correct_content(self):
        driver_list = Driver.objects.all()
        response = self.client.get(DRIVER_LIST_URL)

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            list(response.context["driver_list"]),
            list(driver_list)
        )
        self.assertTemplateUsed(
            response,
            "taxi/driver_list.html"
        )

    def test_driver_list_has_pagination(self):
        self.driver3 = get_user_model().objects.create_user(
            username="dustin.henderson",
            license_number="DUS25131",
            first_name="Dustin",
            last_name="Henderson",
            password="3edcbgt5"
        )

        response = self.client.get(
            DRIVER_LIST_URL,
            {"page": 2}
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_driver_detail_response(self):
        response = self.client.get(reverse("taxi:driver_detail", args=[self.driver2.id]))

        self.assertEqual(
            response.status_code,
            200
        )
