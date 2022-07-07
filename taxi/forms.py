from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Car, Driver


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"


class DriverUpdateLicenseNumberForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise ValidationError("Consist only of 8 characters")
        if not license_number[:3].isalpha() or not license_number[:3].isupper():
            raise ValidationError("First 3 characters are uppercase letters")
        if not license_number[3:].isdigit():
            raise ValidationError("Last 5 characters are digits")

        return license_number


class DriverForm(UserCreationForm, DriverUpdateLicenseNumberForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number", "first_name", "last_name"
        )
