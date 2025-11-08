from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from taxi.models import Car, Manufacturer
from .forms import CarForm, ManufacturerForm

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "car_form.html"
    success_url = reverse_lazy("taxi:car-list")

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car_form.html"
    success_url = reverse_lazy("taxi:car-list")

class CarDeleteView(DeleteView):
    model = Car
    template_name = "car_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-list")

class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = "manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")

