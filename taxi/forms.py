from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div

from .models import Manufacturer, Car


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div("name", css_class="form-group col-4"),
            Div("country", css_class="form-group col-4"),
            Submit("submit", "Save", css_class="mt-4"),
        )


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div("model", css_class="form-group col-4"),
            Div("manufacturer", css_class="form-group col-4"),
            Div("drivers", css_class="form-group col-4"),
            Submit("submit", "Save", css_class="mt-4"),
        )
