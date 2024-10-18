from django import forms

from .models import Manufacturer, Driver

class CarForm(forms.Form):
    model = forms.CharField(max_length=255)
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())  # Поле вибору для існуючих виробників
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
        label="Drivers",
    )

