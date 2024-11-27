from django import forms
from django.contrib.auth import get_user_model

from taxi.models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ("name", "country", )

