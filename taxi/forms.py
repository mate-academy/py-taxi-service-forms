from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from taxi.models import Driver


def check_license_number(number: str):
    if not number[0:3].isalpha() or not number[0:3].isupper():
        raise ValidationError("First 3 letters must be capitals")
    elif not number[3:9].isdigit():
        raise ValidationError("Last 5 letters must be digits")

    return number


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",)

    def clean_license_number(self):
        return check_license_number(self.cleaned_data["license_number"])


class DriverUpdateLicenseForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        return check_license_number(self.cleaned_data["license_number"])


class SearchFieldForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )
