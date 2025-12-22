from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Manufacturer, Driver


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
    return render(request, "taxi/index.html", context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    template_name = "taxi/car_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-list")


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    template_name = "driver/driver_list.html"
    context_object_name = "driver_list"


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    template_name = "driver/driver_detail.html"
    context_object_name = "driver"


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car
    template_name = "car/car_detail.html"
    context_object_name = "car"
