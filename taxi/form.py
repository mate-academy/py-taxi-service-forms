from django import forms

from taxi.models import Car, Driver, Manufacturer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = "__all__"


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
