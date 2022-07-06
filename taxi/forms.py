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
        first_three = all([True if (s.isupper() and s.isalpha()) else False for s in license_number[:3]])
        last_five = all([True if n.isdigit() else False for n in license_number[3:9]])
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

