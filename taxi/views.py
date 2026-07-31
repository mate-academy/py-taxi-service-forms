from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Car, Driver, Manufacturer


@login_required
def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits

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
    paginate_by = 5


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related(
        "manufacturer"
    ).order_by("id")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.order_by("id")


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        "cars__manufacturer"
    )


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = ("model", "manufacturer", "drivers")
    template_name = "taxi/car_format_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = ("model", "manufacturer", "drivers")
    template_name = "taxi/car_format_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    template_name = "taxi/car_delete.html"
    success_url = reverse_lazy("taxi:car-list")


class ManufacturersCreateView(
    LoginRequiredMixin,
    generic.CreateView,
):
    model = Manufacturer
    fields = ("name", "country")
    template_name = "taxi/manufacturers_format_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturersUpdateView(
    LoginRequiredMixin,
    generic.UpdateView,
):
    model = Manufacturer
    fields = ("name", "country")
    template_name = "taxi/manufacturers_format_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturersDeleteView(
    LoginRequiredMixin,
    generic.DeleteView,
):
    model = Manufacturer
    template_name = "taxi/manufacturer_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")
