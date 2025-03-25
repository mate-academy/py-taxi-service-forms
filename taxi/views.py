from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Car, Manufacturer, Driver
from .forms import (
    CarForm,
    ManufacturerForm,
    DriverCreationForm,
    DriverUpdateForm
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "taxi/index.html", context=context)


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "cars"


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = True
        return context


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = False
        return context


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "taxi/car_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturers"


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = True
        return context


class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = False
        return context


class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    form_class = DriverCreationForm
    template_name = "taxi/driver_form.html"
    success_url = reverse_lazy("taxi:driver-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = True
        return context


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    form_class = DriverUpdateForm
    template_name = "taxi/driver_form.html"
    success_url = reverse_lazy("taxi:driver-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_create"] = False
        return context


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = "taxi/driver_confirm_delete.html"
    success_url = reverse_lazy("taxi:driver-list")


class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"


class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"
