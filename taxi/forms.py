from django import forms

from taxi.models import Car, Manufacturer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ("drivers",)


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
