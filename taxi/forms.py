from django.forms import ModelForm

from taxi.models import Car, Manufacturer


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"



