from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
