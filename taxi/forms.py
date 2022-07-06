from django import forms
from django.core.validators import RegexValidator

from taxi.models import Driver


class DriverCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    license_number = forms.CharField(required=True,
                                     min_length=8,
                                     max_length=8,
                                     validators=[
                                         RegexValidator("^[A-Z]{3}\d{5}")])

    class Meta:
        model = Driver
        fields = ["username", "password", "first_name", "last_name", "email",
                  "license_number"]
        # Question to mentors: how I can get current logged on user fields?
        # if model.is_superuser:
        #     fields.append("is_superuser")
        #     fields.append("is_staff")


class DriverUpdateForm(forms.ModelForm):
    license_number = forms.CharField(required=True,
                                     min_length=8,
                                     max_length=8,
                                     validators=[
                                         RegexValidator("^[A-Z]{3}\d{5}")])

    class Meta:
        model = Driver
        fields = ["license_number", ]
