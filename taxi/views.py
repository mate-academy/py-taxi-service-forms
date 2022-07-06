from .forms import CarForm, ManufacturerForm, DriverForm, DriverUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

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
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 2


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


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    form_class = CarForm
    template_name = "taxi/car_form.html"


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-list")

class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    model = Driver
    form_class = DriverForm
    template_name = "taxi/driver_form.html"


class DriverUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Driver
    form_class = DriverUpdateForm
    template_name = "taxi/driver_update_license_number.html"


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Driver
    fields = "__all__"
    template_name = "taxi/driver_confirm_delete.html"
    success_url = reverse_lazy("taxi:driver-list")
