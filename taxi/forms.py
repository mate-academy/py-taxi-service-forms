from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Manufacturer, Car


class DriverForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", "first_name", "last_name")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) == 8 and license_number[:3].isupper() and license_number[3:].isdigit():
            return license_number
        raise ValidationError("Ensure that value is incorrect")


class DriverUpdateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) == 8 and license_number[:3].isupper() and license_number[3:].isdigit():
            return license_number
        raise ValidationError("Ensure that value is incorrect")


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
