from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from taxi.models import Driver


def validate_license_number(number):
    if not len(number) == 8:
        raise ValidationError("License number should consist of 8 characters")
    elif not number[:3].isupper() or not number[:3].isalpha():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not number[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")
    return number


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


class DriverCreateForm(UserCreationForm):

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + \
            ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])
