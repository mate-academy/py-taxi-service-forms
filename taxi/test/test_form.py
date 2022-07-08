from django.test import TestCase
import pytest

from taxi.forms import DriverForm, DriverLicenseUpdateForm


class DriverFormsTest(TestCase):
    def test_driver_creation_form_with_license_number_first_last_name_is_valid(
            self):
        form_data = {
            "username": "new_user",
            "password1": "1234user",
            "password2": "1234user",
            "first_name": "Test",
            "last_name": "test",
            "license_number": "QWE12345"
        }
        form = DriverForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_license_number_is_valid(self):
        form = DriverLicenseUpdateForm(data={"license_number": "QWE12345"})
        self.assertTrue(form.is_valid())

    def test_license_number_check_validation(self):
        parameters = ("qwe12345",
                      "QW12345",
                      "Qwq12345",
                      "QWER2345",
                      "QWE1234",
                      "QWE123485",
                      "12345678",
                      "qwertyui")
        for parameter in parameters:
            form = DriverLicenseUpdateForm(data={"license_number": parameter})
            self.assertFalse(form.is_valid())
