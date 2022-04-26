from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import DriverLicenseForm
from .models import Driver, Car, Manufacturer


@login_required
def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 2


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:index")


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:index")


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:index")


class CarCreateView(CreateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:index")


class CarUpdateView(UpdateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:index")


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:index")


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 2
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 2


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverCreateView(CreateView):
    model = Driver
    template_name = "taxi/driver_form.html"
    fields = ["username", "password", "license_number"]
    success_url = reverse_lazy("taxi:index")


class DriverUpdateView(UpdateView):
    model = Driver
    form_class = DriverLicenseForm
    template_name = "taxi/driver_form.html"
    success_url = reverse_lazy("taxi:index")


class DriverDeleteView(DeleteView):
    model = Driver
    success_url = reverse_lazy("taxi:index")
