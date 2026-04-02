from django import forms

from .models import Manufacturer, Driver, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=255)
    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all(),
        empty_label="Select a manufacturer",
        to_field_name="id"
    )
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.exclude
        (license_number__isnull=True).exclude(license_number__exact=""),
        widget=forms.CheckboxSelectMultiple
    )


class ManufacturerForm(forms.Form):
    name = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
