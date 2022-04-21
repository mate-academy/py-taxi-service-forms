from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from taxi.models import Driver


class DriverLicenseUpdate(forms.ModelForm):
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
