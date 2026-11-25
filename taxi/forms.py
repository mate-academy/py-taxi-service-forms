from django import forms
from crispy_forms.helper import FormHelper

from .models import Manufacturer
from .views import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("name", "manufacturer")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ("name", "manufacturer")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
