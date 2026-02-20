from django.forms import ModelForm

from taxi.models import Manufacturer, Car


class FormCar(ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]


class FormManufacturer(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]
