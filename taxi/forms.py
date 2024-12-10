from django import forms
from .models import Car, Manufacturer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"  # Adjust fields based on my model


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"  # Adjust fields based on my model
