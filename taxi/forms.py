from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Car, Driver


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"


def checking_license_number(license_number):

    if len(license_number) != 8:
        raise ValidationError("License number should consist of 8 digits")

    if license_number[0:3].isupper() is False:
        raise ValidationError("First 3 digits should be uppercase")

    if license_number[3:].isnumeric() is False:
        raise ValidationError("Last 5 digits should be numbers")

    return license_number


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", "first_name", "last_name")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return checking_license_number(license_number)


class LicenseForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return checking_license_number(license_number)
