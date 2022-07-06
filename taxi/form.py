from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        if len(license_number) != 8:
            raise ValidationError("License number should consist of 8 digits")

        if license_number[0:3].isupper() is False:
            raise ValidationError("First 3 digits should be uppercase")
        if license_number[3:].isnumeric() is False:
            raise ValidationError("Last 5 digits should be numbers")
        return license_number
