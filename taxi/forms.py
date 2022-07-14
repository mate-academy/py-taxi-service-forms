from django.contrib.auth.forms import UserCreationForm
from django import forms

from taxi.models import Driver


def validate_license_number(license_number: str):
    error = "Password requirements: Password should be 8 characters long, " \
            "first 3 characters should be uppercase, " \
            "Last 5 characters should be digits"

    if len(license_number) != 8:
        raise forms.ValidationError(error)
    elif not license_number[:3].isupper() or not license_number[:3].isalpha():
        raise forms.ValidationError(error)
    elif not license_number[5:].isdigit():
        raise forms.ValidationError(error)

    return license_number


class DriverCreationForm(UserCreationForm):

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number", "first_name", "last_name",
        )

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class LicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(required=True)

    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])
