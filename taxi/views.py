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


class IndexView(TemplateView):
    template_name = "taxi/index.html"


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"


class CarCreateView(CreateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("car-list")


class CarUpdateView(UpdateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("car-list")


class CarDeleteView(DeleteView):
    model = Car
    template_name = "taxi/car_confirm_delete.html"
    success_url = reverse_lazy("car-list")


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("manufacturer-list")


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("manufacturer-list")


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("manufacturer-list")


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"
