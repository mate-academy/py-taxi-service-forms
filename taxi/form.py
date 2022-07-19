from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from taxi.expansion import license_validation
from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        max_length=8,
        required=True,
        help_text="<li>License number must contain exactly 8 characters</li>"
                  "<li>First 3 characters are uppercase letters</li>"
                  "<li>Last 5 characters are digits</li>",
    )

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "license_number",
        )

    @license_validation
    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("license_number",)

    @license_validation
    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"
