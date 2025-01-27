from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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
        "num_visits": num_visits + 1,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer/manufacturer_list.html"
    paginate_by = 5


class ManufacturerAddView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/add.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/update.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/delete.html"


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car/car_list.html"
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = "taxi/car/car_detail.html"


class CarAddView(LoginRequiredMixin, CreateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/add.html"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/update.html"

    def get_success_url(self):
        return reverse_lazy("taxi:car-detail", kwargs={"pk": self.object.pk})


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/delete.html"


class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver/driver_list.html"


class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver
    template_name = "taxi/driver/driver_detail.html"
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
