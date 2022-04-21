from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import ModelForm

from taxi.models import Driver, Car, Manufacturer


class DriverCreateForm(UserCreationForm):
    LICENSE_CHARACTERS = 8
    license_number = forms.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(LICENSE_CHARACTERS),
            MaxLengthValidator(LICENSE_CHARACTERS)
        ]
    )

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields = ("license_number", "first_name", "last_name",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if not license_number[:3].isupper():
            raise ValidationError("First 3 characters must be in uppercase.")

        if not license_number[3:].isdigit():
            raise ValidationError("Last 5 characters must be digits.")

        return license_number


class DriverUpdateForm(UserChangeForm):

    class Meta:
        model = Driver
        fields = UserChangeForm.Meta.fields = ("username", "first_name", "last_name",)


class DriverLicenseUpdateForm(forms.ModelForm):
    LICENSE_CHARACTERS = 8
    license_number = forms.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(LICENSE_CHARACTERS),
            MaxLengthValidator(LICENSE_CHARACTERS)
        ]
    )

    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if not license_number[:3].isupper():
            raise ValidationError("First 3 characters must be in uppercase.")

        if not license_number[3:].isdigit():
            raise ValidationError("Last 5 characters must be digits.")

        return license_number


class CarCreateForm(ModelForm):

    class Meta:
        model = Car
        fields = "__all__"


class ManufacturerCreateForm(ModelForm):

    class Meta:
        model = Manufacturer
        fields = "__all__"
