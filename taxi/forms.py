from django import forms
from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from taxi.models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save"))
