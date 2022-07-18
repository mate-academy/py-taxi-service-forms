from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


def clean_license_number(license_number):
    if len(license_number) != 8:
        raise ValidationError(
            "License number should consist of 8 characters exactly"
        )
    elif not license_number[:3].isupper():
        raise ValidationError(
            "First 3 characters of license number "
            "should be uppercase letters"
        )
    elif not license_number[3:].isdigit():
        raise ValidationError(
            "Last 5 characters of license number should be digits"
        )


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        validators=[clean_license_number],
        help_text="Consists of 8 characters: "
                  "first 3 – uppercase letters, last 5 – digits."
    )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "license_number",
        )


class LicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        validators=[clean_license_number],
        help_text="Consists of 8 characters: "
                  "first 3 – uppercase letters, last 5 – digits."
    )

    class Meta:
        model = Driver
        fields = ("license_number",)
