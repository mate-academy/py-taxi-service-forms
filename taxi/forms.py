from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from taxi.models import Driver, Car


def clean_license_number(number):
    if not len(number) == 8:
        raise ValidationError("License number should consist of 8 characters")
    elif not number[:3].isupper():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not number[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")
    return number


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
        )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "license_number",
        )


class LicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        validators=[clean_license_number],
        )

    class Meta:
        model = Driver
        fields = ("license_number",)
