from django.contrib.auth.forms import UserCreationForm
from django import forms

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "license_number", "first_name", "last_name",
        )


class LicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(required=True)

    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        data = self.cleaned_data.get("license_number")

        if not data[:3].isupper():
            raise forms.ValidationError("First 3 letters should be uppercase")
        elif not data[5:].isdigit():
            raise forms.ValidationError("Last 5 letters should be numbers")
        elif len(data) != 8:
            raise forms.ValidationError("Password should be 8 symbols long")

        return data
