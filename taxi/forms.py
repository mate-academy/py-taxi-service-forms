from django import forms
from .models import Car, Manufacturer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))

    class Meta:
        model = Car
        fields = "__all__"


class ManufacturerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))

    class Meta:
        model = Manufacturer
        fields = "__all__"
