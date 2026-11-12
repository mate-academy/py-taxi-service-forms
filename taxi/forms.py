from django import forms

from taxi.models import Car, Manufacturer


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["manufacturer", "model", "drivers"]


class UpdateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["manufacturer", "model", "drivers"]


class CreateManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]


class UpdateManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]
