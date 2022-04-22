from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverForm(forms.ModelForm):
    MIN_LICENSE_CHARACTERS = 8

    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != DriverForm.MIN_LICENSE_CHARACTERS:
            raise ValidationError(f"License has to consist only {DriverForm.MIN_LICENSE_CHARACTERS}")

        if not license_number[:3].isupper() or not license_number[:3].isalpha():
            raise ValidationError("The first 3 characters have to be UpperCase")

        if license_number[-5:].isdigit() is False:
            raise ValidationError("The last 5 characters have to be digit")

        return license_number


