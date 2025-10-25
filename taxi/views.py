from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView

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


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    paginate_by = 5


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class CarCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")

    def test_func(self):
        return True


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")

    def test_func(self):
        return True


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")

    def test_func(self):
        return True


class ManufacturerCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")

    def test_func(self):
        return True


class ManufacturerUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")

    def test_func(self):
        return True


class ManufacturerDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")

    def test_func(self):
        return True
