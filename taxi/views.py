from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

import taxi
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


class CarFormatListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "taxi/car_format_list.html"
    context_object_name = "car_format_list"


class CarFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-format-list")
    template_name = "taxi/car_format_form.html"


class CarFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-format-list")
    template_name = "taxi/car_format_form.html"


class CarFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    template_name = "taxi/car_format_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-format-list")


class ManufacturerFormatListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_format_list.html"
    context_object_name = "manufacturer_format_list"


class ManufacturerFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-format-list")
    template_name = "taxi/manufacturer_form.html"


class ManufacturerFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-format-list")
    template_name = "taxi/manufacturer_form.html"


class ManufacturerFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-format-list")
