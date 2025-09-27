from django import forms

from taxi.models import Car, Manufacturer


class CarForm(forms.ModelForm):
    model = Car
    fields = "__all__"


class ManufacturerForm(forms.ModelForm):
    model = Manufacturer
    fields = "__all__"
