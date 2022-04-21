from django import forms

from taxi.models import Driver
from taxi.validators import license_number_validator


class DriverLicenseForm(forms.ModelForm):
    license_number = forms.CharField(validators=[license_number_validator])

    class Meta:
        model = Driver
        fields = []