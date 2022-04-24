from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number",
            "first_name",
            "last_name",
        )


class DriverUpdateForm(forms.ModelForm):
    LICENSE_LENGTH = 8

    class Meta:
        model = Driver
        fields = ("username", "license_number", "first_name", "last_name")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != DriverUpdateForm.LICENSE_LENGTH:
            raise ValidationError(
                "The serial number of the license consists of 8 characters!"
            )

        if not license_number[:3].isupper():
            raise ValidationError(
                "The first three characters must be "
                "uppercase, for example: AAA***** ."
            )

        if not license_number[-5:].isdigit():
            raise ValidationError("The last 5 characters must be numbers!")

        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"
