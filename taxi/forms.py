from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from taxi.models import Driver


class DriverCreateForm(UserCreationForm):
    license_number = forms.CharField(required=True,
                                     min_length=8,
                                     max_length=8,
                                     help_text="License format: AAA00000",
                                     validators=[
                                         RegexValidator("^[A-Z]{3}\d{5}")])

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("first_name",
                                                 "last_name",
                                                 "license_number")


class DriverUpdateForm(forms.ModelForm):
    license_number = forms.CharField(required=True,
                                     min_length=8,
                                     max_length=8,
                                     validators=[
                                         RegexValidator("^[A-Z]{3}\d{5}")])

    class Meta:
        model = Driver
        fields = ["license_number", ]
