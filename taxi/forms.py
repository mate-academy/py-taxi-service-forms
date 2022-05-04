from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django import forms

from taxi.models import Driver, Car


def clean_license_number(license_number):

    if len(license_number) != 8:
        raise ValidationError("The license number should consist only of 8 characters.")

    if not (license_number[:3].isalpha()
            and license_number[:3].isupper()):
        raise ValidationError("First 3 characters should be uppercase letters.")

    if not license_number[-5:].isdigit():
        raise ValidationError("Last 5 characters should be a digits.")

    return license_number


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        validators=[clean_license_number],
        help_text="License number should consist only of 8 characters: first 3 - uppercase letters, last 5 - digits. "
                  "For example: AAA00000"
    )

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "license_number"
        )


class DriverUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        validators=[clean_license_number],
        help_text="License number should consist only of 8 characters: first 3 - uppercase letters, last 5 - digits. "
                  "For example: AAA00000"
    )

    class Meta:
        model = Driver
        fields = ("first_name", "last_name", "username", "license_number", "email")


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
