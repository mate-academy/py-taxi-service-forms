from django import forms

from taxi.models import Car, Manufacturer
import crispy_bootstrap4


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
