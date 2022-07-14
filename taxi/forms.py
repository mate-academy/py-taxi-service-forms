from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe

from taxi.models import Driver


class DriverCreateForm(UserCreationForm):
    license_number = forms.CharField(
        required=True,
        min_length=8,
        max_length=8,
        help_text=mark_safe(
            f"License number format: <strong>AAA00000</strong><br><ul>"
            f"<li>3 capital A-Z at the start</li>"
            f"<li>5 digits at the end</li>"
            f"<li>full length: 8 characters</li></ul>"),
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
