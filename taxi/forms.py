from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from taxi.models import Driver


def check_license(license_number):
    if len(license_number) != 8 or not license_number[:3].isupper() or not license_number[3:].isnumeric():
        raise ValidationError("License number must consist only of 8 characters, "
                              "first 3 characters are uppercase letters, "
                              "last 5 characters are digits")
    return license_number


class DriverCreationForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        return check_license(license_number)


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        return check_license(license_number)
