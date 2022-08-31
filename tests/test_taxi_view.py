from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer

MANUFACTURER_LIST_URL = reverse("taxi:manufacturer-list")
DRIVER_LIST_URL = reverse("taxi:driver-list")
CAR_LIST_URL = reverse("taxi:car-list")


class ManufacturerListTest(TestCase):
    fixtures = ["taxi_service_db_data.json", ]

    def test_manufacturer_list_response_with_correct_template(self):
        response = self.client.get(MANUFACTURER_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/manufacturer_list.html")

    def test_manufacturer_list_paginated_by_2(self):
        response = self.client.get(MANUFACTURER_LIST_URL)

        self.assertEqual(len(response.context["manufacturer_list"]), 2)

    def test_manufacturer_list_ordered_by_name(self):
        response = self.client.get(MANUFACTURER_LIST_URL)
        man_list = Manufacturer.objects.all().order_by("name")

        self.assertEqual(
            list(response.context["manufacturer_list"]),
            list(man_list[:2])
        )


class CarListTest(TestCase):
    fixtures = ['taxi_service_db_data.json', ]

    def test_car_list_response_with_correct_template(self):
        response = self.client.get(CAR_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/car_list.html")

    def test_car_list_paginated_by_2(self):
        response = self.client.get(CAR_LIST_URL)
        self.assertEqual(len(response.context["car_list"]), 2)

    def test_car_detail_response_with_correct_template(self):
        response = self.client.get(reverse("taxi:car-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/car_detail.html")


class DriverListTest(TestCase):
    fixtures = ['taxi_service_db_data.json', ]

    def test_car_list_response_with_correct_template(self):
        response = self.client.get(DRIVER_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/driver_list.html")

    def test_car_list_paginated_by_2(self):
        response = self.client.get(DRIVER_LIST_URL)
        self.assertEqual(len(response.context["driver_list"]), 2)

    def test_car_detail_response_with_correct_template(self):
        response = self.client.get(reverse("taxi:driver-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/driver_detail.html")
