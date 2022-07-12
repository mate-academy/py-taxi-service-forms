from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django import forms

from .models import Driver


class DriverUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields = (
            "username",
            "license_number",
            "first_name",
            "last_name",
        )


class DriverLicenseUpdateForm(ModelForm):
    license_number = forms.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex="[A-D]{3}[0-9]{5}",
                message="Enter correct value like AAA00000"
            ),
        ]
     )

    class Meta:
        model = Driver
        fields = ("license_number", )
