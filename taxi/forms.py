from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.forms import CheckboxSelectMultiple

from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number", "first_name", "last_name")


class DriverUpdateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = ("username", "first_name", "last_name",)


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        first_three = all([license_number[:3].isupper(), license_number[:3].isalpha()])
        last_five = license_number[3:9].isdigit()
        if not first_three or len(license_number) != 8 or not last_five:
            raise ValidationError("Incorrect License number!")
        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"

