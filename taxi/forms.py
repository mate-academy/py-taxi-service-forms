from django import forms
from .models import Car, Manufacturer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Car Details",
                "model",
                "manufacturer",
                "drivers",
            ),
            Submit("submit", "Save Car")
        )
class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Manufacturer Information",
                "name",
                "country",
            ),
            Submit("submit", "Save Manufacturer")
        )
