from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from taxi.models import Driver


def validate_license_number(license_number):
    if len(license_number) != 8:
        raise ValidationError("License must consist only of 8 characters")
    elif not license_number[:3].isupper() or not license_number[:3].isalpha():
        raise ValidationError("First 3 characters must be uppercase letters")
    elif not license_number[3:].isdigit():
        raise ValidationError("Last 5 characters must be digits")
    return license_number


class DriverCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "license_number")

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])
