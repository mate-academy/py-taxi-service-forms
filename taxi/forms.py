from django import forms
from .models import Car, Manufacturer, Driver
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django.contrib.auth.forms import UserCreationForm, UsernameField


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("name"),
            Field("country"),
            Submit("submit", "Save")
        )


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("model"),
            Field("manufacturer"),
            Field("drivers"),
            Submit("submit", "Save")
        )


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "License Number"})
    )
    first_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Last Name"})
    )

    class Meta:
        model = Driver
        fields = ("username", "first_name", "last_name", "license_number")
        field_classes = {"username": UsernameField}  # recommended by Django

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("username"),
            Field("first_name"),
            Field("last_name"),
            Field("license_number"),
            "password",  # Important: Include password fields
            "password2",
            Submit("submit", "Create")
        )


class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["first_name", "last_name", "license_number"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("first_name"),
            Field("last_name"),
            Field("license_number"),
            Submit("submit", "Update")
        )
