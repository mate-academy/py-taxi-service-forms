from django import forms
from taxi.models import Car, Manufacturer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
