from taxi.models import Manufacturer, Car
from django import forms


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
