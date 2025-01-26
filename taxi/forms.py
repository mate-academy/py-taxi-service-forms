from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django import forms

from taxi.models import Manufacturer, Car



class ManufacturerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

    class Meta:
        model = Manufacturer
        fields = ["name", "country"]
        widgets = {
        }


class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.helper.add_input(Submit(name="submit", value="Submit"))

    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(
                attrs={"class": "form-select drivers-field", "size": "5"}
            )
        }
