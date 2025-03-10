from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['manufacturer'].widget.attrs['class'] = 'form-control'
        self.fields['model'].widget.attrs['class'] = 'form-control'
