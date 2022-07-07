from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "license_number")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise ValidationError("License number must be 8 characters long")
        if not license_number[:3].isalpha() or not license_number[:3].isupper():
            raise ValidationError("License number must start with 3 upper case letters")
        if not license_number[3:].isdigit():
            raise ValidationError("License number must end with 5 digits only")
        return license_number
