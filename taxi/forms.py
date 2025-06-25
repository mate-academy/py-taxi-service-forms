from django import forms
from .models import Car, Manufacturer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["manufacturer", "model"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))

    def save(self, commit=True):
        car = super().save(commit=False)
        if self.user:
            car.driver = self.user
        if commit:
            car.save()
        return car


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))
