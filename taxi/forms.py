from crispy_forms.helper import FormHelper
from django import forms
from .models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = "post"
