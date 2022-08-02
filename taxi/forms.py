from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'license_number',)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return check_license_number(license_number)


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all(),
                                             widget=forms.CheckboxSelectMultiple,
                                             required=False)

    class Meta:
        model = Car
        fields = "__all__"


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return check_license_number(license_number)


def check_license_number(number):
    if len(number) != 8:
        raise ValidationError("License must have 8 digits.")
    if not number[:3].isupper():
        raise ValidationError("First 3 characters must be upper letters.")
    if not number[3:].isdigit():
        raise ValidationError("Last 5 characters must be numbers.")
    return number
