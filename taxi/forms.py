from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver


def validate_license_number(license_number):
    if (len(license_number) == 8
            and license_number[:3].isalpha()
            and license_number[:3] == license_number[:3].upper()
            and license_number[3:].isdigit()
    ):
        return license_number
    else:
        raise ValidationError("the license number must be valid")


class DriverCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number")

    def clean_license_number(self):

        license_number = self.cleaned_data["license_number"]
        return validate_license_number(license_number)


class LicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):

        license_number = self.cleaned_data["license_number"]
        return validate_license_number(license_number)
