from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from taxi.forms import CarForm
from taxi.models import Car, Manufacturer, Driver


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"


class ManufacturerCreateView(generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarCreateView(generic.CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(generic.UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


def index(request):
    """View function for the home page of the site."""
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)
