from django import forms
from .models import Car, Manufacturer, Driver
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("name"),
            Field("country"),
            Submit("submit", "Save")
        )


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field("model"),
            Field("manufacturer"),
            Field("drivers"),
            Submit("submit", "Save")
        )
