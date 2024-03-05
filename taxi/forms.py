from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Car, Manufacturer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save Car"))


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ManufacturerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save Manufacturer"))
