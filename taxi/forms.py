from django import forms
from .models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
