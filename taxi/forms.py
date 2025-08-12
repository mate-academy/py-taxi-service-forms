from django import forms
from .models import Manufacturer, Car


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ("name", "country")


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("model", "manufacturer", "drivers")
        widgets = {
            "drivers": forms.CheckboxSelectMultiple
        }
