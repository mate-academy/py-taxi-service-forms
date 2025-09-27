from django import forms
from django.contrib.auth import get_user_model

from .models import Car, Manufacturer


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.none(),  # Queryset inicial vazio
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["drivers"].queryset = get_user_model().objects.all()

    class Meta:
        model = Car
        fields = "__all__"
