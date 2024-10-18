from django import forms

class CarForm(forms.Form):
    model = forms.CharField(max_length=255)
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())  # Поле вибору для існуючих виробників
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )  # Множинний вибір водіїв