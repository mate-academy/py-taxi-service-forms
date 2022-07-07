from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Car, Driver


class DriverCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        return validate_license_number(license_number)


class DriverLicenseUpdateForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        return validate_license_number(license_number)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"


def validate_license_number(license_number):
    if not len(license_number) == 8:
        raise ValidationError("Ensure that length of license equals 8")

    for char in license_number[:3]:
        if not char.isalpha():
            raise ValidationError("Ensure that first 3 characters are letters")

        if not char.isupper():
            raise ValidationError("Ensure that first 3 characters are uppercase")

    for char in license_number[3:]:
        if not char.isdigit():
            raise ValidationError("Ensure that last 5 characters are digits")

    return license_number
