from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.forms import CarForm
from taxi.models import Car, Manufacturer


class FormViewsTests(TestCase):
    def setUp(self):
        self.driver = get_user_model().objects.create_user(
            username="driver", license_number="ABC12345"
        )
        self.manufacturer = Manufacturer.objects.create(
            name="Lincoln", country="USA"
        )
        self.car = Car.objects.create(
            model="Continental", manufacturer=self.manufacturer
        )
        self.car.drivers.add(self.driver)
        self.client.force_login(self.driver)

    def test_all_mutation_views_require_login(self):
        self.client.logout()
        for model, instance in (
            ("car", self.car), ("manufacturer", self.manufacturer)
        ):
            for action in ("create", "update", "delete"):
                url = reverse(
                    f"taxi:{model}-{action}",
                    kwargs={} if action == "create" else {"pk": instance.pk},
                )
                for method in (self.client.get, self.client.post):
                    with self.subTest(url=url, method=method.__name__):
                        response = method(url)
                        self.assertRedirects(
                            response, f"/accounts/login/?next={url}",
                            fetch_redirect_response=False,
                        )
        self.assertTrue(Car.objects.filter(pk=self.car.pk).exists())
        self.assertEqual(Manufacturer.objects.count(), 1)

    def test_form_pages_render_and_update_is_prefilled(self):
        for model, instance in (
            ("car", self.car), ("manufacturer", self.manufacturer)
        ):
            for action in ("create", "update"):
                with self.subTest(model=model, action=action):
                    response = self.client.get(reverse(
                        f"taxi:{model}-{action}",
                        kwargs=(
                            {} if action == "create"
                            else {"pk": instance.pk}
                        ),
                    ))
                    self.assertEqual(response.status_code, 200)
                    self.assertContains(response, "csrfmiddlewaretoken")
                    self.assertContains(response, "form-group")
                    if action == "update":
                        self.assertEqual(response.context["form"].instance,
                                         instance)
        response = self.client.get(reverse(
            "taxi:car-update", kwargs={"pk": self.car.pk}
        ))
        self.assertEqual(list(response.context["form"]["drivers"].value()),
                         [self.driver.pk])

    def test_invalid_car_does_not_save(self):
        response = self.client.post(reverse("taxi:car-create"), {
            "model": "", "manufacturer": self.manufacturer.pk,
            "drivers": [self.driver.pk],
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("model", response.context["form"].errors)
        self.assertEqual(Car.objects.count(), 1)
        form = CarForm(data={
            "model": "Car", "manufacturer": self.manufacturer.pk,
            "drivers": [self.driver.pk + 100],
        })
        self.assertFalse(form.is_valid())
        self.assertIn("drivers", form.errors)

    def test_duplicate_manufacturer_does_not_save(self):
        response = self.client.post(reverse("taxi:manufacturer-create"), {
            "name": "Lincoln", "country": "USA",
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", response.context["form"].errors)
        self.assertEqual(Manufacturer.objects.count(), 1)

    def test_delete_get_only_confirms_and_has_cancel(self):
        for model, instance, cancel in (
            ("car", self.car, reverse("taxi:car-detail",
                                      kwargs={"pk": self.car.pk})),
            ("manufacturer", self.manufacturer,
             reverse("taxi:manufacturer-list")),
        ):
            response = self.client.get(reverse(
                f"taxi:{model}-delete", kwargs={"pk": instance.pk}
            ))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, f'href="{cancel}"')
            self.assertContains(response, "csrfmiddlewaretoken")
            self.assertTrue(type(instance).objects.filter(
                pk=instance.pk).exists())

    def test_car_update_replaces_driver_assignments(self):
        other = get_user_model().objects.create_user(
            username="other", license_number="XYZ12345"
        )
        response = self.client.post(reverse(
            "taxi:car-update", kwargs={"pk": self.car.pk}
        ), {"model": "Updated", "manufacturer": self.manufacturer.pk,
            "drivers": [other.pk]})
        self.assertRedirects(response, reverse("taxi:car-list"))
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, "Updated")
        self.assertEqual(list(self.car.drivers.all()), [other])

    def test_missing_objects_return_404(self):
        for model in ("car", "manufacturer"):
            for action in ("update", "delete"):
                self.assertEqual(self.client.get(reverse(
                    f"taxi:{model}-{action}", kwargs={"pk": 999}
                )).status_code, 404)
