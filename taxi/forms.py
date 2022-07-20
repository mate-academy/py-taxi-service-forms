from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


class DriverCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "licence_number",
        )

    def clean_licence_number(self):
        return validate_licence_number(self.cleaned_data["licence_number"])


class DriverLicenceUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["licence_number"]

    def clean_licence_number(self):
        return validate_licence_number(self.cleaned_data["licence_number"])


def validate_licence_number(licence):
    licence_number = licence
    letters = licence_number[0:3].isupper()
    numbers = licence_number[3:].isnumeric()
    if len(licence_number) == 8 and letters and numbers:
        return licence_number
    raise ValidationError(
        "- There must be 8 symbols!"
        " First 3 symbols must be alphabets in upper case!"
        " Last 5 symbols must be numeric!"
    )


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = "__all__"


class CarSearchForm(forms.Form):
    model = forms.CharField(
        max_length=150,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search car..."})
    )


class DriverSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=50,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )
