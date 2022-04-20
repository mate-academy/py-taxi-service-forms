from django.contrib.auth.forms import UserCreationForm
from django.forms import models

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    MIN_LENGTH = 8

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) < DriverCreationForm.MIN_LENGTH:
            raise ValueError("License number should be greater or equal than 8")
        if not license_number[:3].isupper():
            raise ValueError("First 3 letters should be uppercase")

        if not license_number[-5:].isdigit():
            raise ValueError("Last 5 characters should be uppercase")

        return license_number
