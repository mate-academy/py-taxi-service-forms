from django.test import TestCase

from taxi.forms import DriverUpdateLicenseForm


class FormsTest(TestCase):

    def test_form_update_license(self):
        form_data = {
            "license_number": "AAA12345"
        }
        form = DriverUpdateLicenseForm(data=form_data)
        self.assertTrue(form.is_valid())
