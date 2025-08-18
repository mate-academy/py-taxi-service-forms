from crispy_forms.helper import FormHelper
from django import forms
from .models import Car, Manufacturer


class CarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Car
        fields = "__all__"


class ManufacturerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Manufacturer
        fields = "__all__"
