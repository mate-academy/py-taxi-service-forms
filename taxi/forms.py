from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        return check_license(self.cleaned_data["license_number"])


class DriverCreateForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number")

    def clean_license(self):
        return check_license(self.cleaned_data["license_number"])


def check_license(number):
    if len(number) != 8:
        raise ValidationError("License must have 8 digits.")
    elif not number[:3].isalpha() or not number[:3].isupper():
        raise ValidationError("First 3 characters must be capital letters.")
    elif not number[3:].isdigit():
        raise ValidationError("Last 5 characters must be numbers.")
    return number
