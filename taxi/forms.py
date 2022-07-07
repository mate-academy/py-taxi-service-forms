from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


def validation_license_number(license_number):
    if len(license_number) != 8:
        raise ValidationError("License number should has 8 characters")
    if not license_number[:3].isupper():
        raise ValidationError("License number's first 3 characters should be uppercase letters")
    if not license_number[3:].isdigit():
        raise ValidationError("License number's last 5 characters should be digits")
    return license_number


class DriverCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "license_number",
        )

    def clean_license_number(self):
        return validation_license_number(self.cleaned_data["license_number"])


class LicenceUpdateForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        return validation_license_number(self.cleaned_data["license_number"])


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
