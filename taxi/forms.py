from django import forms

from taxi.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ("drivers",)
