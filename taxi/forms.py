from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from taxi.models import Car, Driver, Manufacturer


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"


class DriverForm(forms.ModelForm):
    LICENSE_LEN = 8
    LETTERS_LICENSE = 3
    DIGITS_LICENSE = 5

    class Meta:
        model = Driver
        fields = ("username", "password", "first_name",
                  "last_name", "license_number")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != DriverForm.LICENSE_LEN:
            raise ValidationError(f"License number should be"
                                  f" {DriverForm.LICENSE_LEN} symbols!")
        if not license_number[:DriverForm.LETTERS_LICENSE].isupper():
            raise ValidationError(f"First {DriverForm.LETTERS_LICENSE} must be"
                                  f" letters in uppercase!")
        if not license_number[:DriverForm.LETTERS_LICENSE].isalpha():
            raise ValidationError(f"First {DriverForm.LETTERS_LICENSE} must be"
                                  f" letters, not contain numbers!")
        if not license_number[-DriverForm.DIGITS_LICENSE:].isdigit():
            raise ValidationError(f"Last {DriverForm.DIGITS_LICENSE} must be"
                                  f" integer numbers!")

        return license_number


class DriverLicenseUpdateForm(DriverForm):
    class Meta:
        model = Driver
        fields = ["license_number"]


class SearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "search ..."})
    )


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
