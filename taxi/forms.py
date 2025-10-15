from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]

        widgets = {
            "model": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter car model"}),
            "manufacturer": forms.Select(attrs={"class": "form-control"}),
            "drivers": forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def clean_model(self):
        model = self.cleaned_data["model"]
        if len(model) < 2:
            raise forms.ValidationError("Model name must have at least 2 characters.")
        return model