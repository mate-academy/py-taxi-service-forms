from django import forms
from .models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["manufacturer", "model", "drivers"]
