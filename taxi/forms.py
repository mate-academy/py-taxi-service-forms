from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Car, Driver, Manufacturer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class DriverForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", "first_name", "last_name")

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"


def validate_license_number(license_num: str):
    if len(license_num) != 8:
        raise ValidationError("License number should contain 8 characters")
    if not license_num[0:3].isupper():
        raise ValidationError("License number should start with 3 capital letters")
    if not license_num[3:].isdigit():
        raise ValidationError("License number should include 5 digits")
    return license_num
