from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_tag = False
        self.helper.layout = Layout(
            *self.fields.keys()
        )
