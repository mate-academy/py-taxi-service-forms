from django import forms

from .models import Manufacturer, Driver, Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
