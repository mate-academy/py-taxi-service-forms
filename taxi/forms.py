from django import forms
from django.forms import ModelForm

from .models import Car, Manufacturer


class CarForm(ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        from .models import Driver
        super().__init__(*args, **kwargs)
        self.fields["drivers"].queryset = Driver.objects.all()


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"
