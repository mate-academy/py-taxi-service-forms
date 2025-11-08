from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Car, Driver, Manufacturer
from .forms import CarForm, ManufacturerForm


class IndexView(TemplateView):
    template_name = "taxi/index.html"


class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("car-list")


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("car-list")


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("car-list")


class ManufacturerListView(ListView):
    model = Manufacturer


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("manufacturer-list")


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("manufacturer-list")


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("manufacturer-list")


class DriverListView(ListView):
    model = Driver


class DriverDetailView(DetailView):
    model = Driver
