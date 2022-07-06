from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


def validate_license_number(driving_license):
    if not len(driving_license) == 8:
        raise ValidationError("License number should consist of 8 characters")
    if not driving_license[:3].isalpha() or not driving_license[:3].isupper():
        raise ValidationError("First 3 characters should be uppercase letters")
    if not driving_license[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")
    return driving_license


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class DriverCreationForm(UserCreationForm):

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + \
            ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
