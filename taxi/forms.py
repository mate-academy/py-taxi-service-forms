from django import forms
from .models import Message, Car, Manufacturer


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content"]


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["name", "country"] 