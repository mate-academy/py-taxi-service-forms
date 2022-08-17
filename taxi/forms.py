from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "license_number")


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise ValidationError("Length license number must be 8 characters")

        for num in license_number[:3]:
            if not num.isalpha() or not num.isupper():
                raise ValidationError("First 3 characters must be uppercase letters")

        for num in license_number[3:]:
            if not num.isnumeric():
                raise ValidationError("Last 5 characters must be digits")

        return license_number
