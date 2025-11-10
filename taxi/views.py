from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Car, Manufacturer, Driver


def index(request):
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_drivers = Driver.objects.count()

    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits

    context = {
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_drivers": num_drivers,
        "num_visits": num_visits,
    }

    return render(request, "taxi/index.html", context)


# -------------------------------
# Manufacturer Views
# -------------------------------
class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")


# -------------------------------
# Car Views
# -------------------------------
class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    context_object_name = "car_list"


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


# -------------------------------
# Driver Views
# -------------------------------
class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    context_object_name = "driver_list"
