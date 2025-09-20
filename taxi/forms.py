from django import forms
from .models import Car, Manufacturer, Driver


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]
        widgets = {
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "manufacturer": forms.Select(attrs={"class": "form-control"}),
            "drivers": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["manufacturer"].queryset = Manufacturer.objects.all()
        self.fields["drivers"].queryset = Driver.objects.all()
        self.fields["drivers"].required = False


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
        }
