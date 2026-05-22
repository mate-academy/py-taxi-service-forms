from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from taxi.models import Car, Manufacturer
from taxi.forms import CarForm, ManufacturerForm


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(DeleteView):
    model = Car
    template_name = "taxi/car_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")
