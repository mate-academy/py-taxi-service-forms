from django import forms
from .models import Car, Manufacturer
from crispy_forms.helper import FormHelper


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
    helper = FormHelper()


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
    helper = FormHelper()
