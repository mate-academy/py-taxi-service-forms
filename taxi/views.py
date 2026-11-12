from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (UpdateCarForm,
                    CreateCarForm,
                    CreateManufacturerForm,
                    UpdateManufacturerForm,
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


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class ManufacturerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manufacturer


class ManufacturerCreateView(
    CreateManufacturerForm,
    LoginRequiredMixin,
    generic.CreateView
):
    model = Manufacturer
    fields = ["name", "country"]
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(
    UpdateManufacturerForm,
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Manufacturer
    fields = "__all__"
    template_name = "taxi/manufacturer_form.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except Exception:
            return HttpResponseRedirect(
                reverse(
                    "taxi:manufacturer-delete",
                    kwargs={"pk": self.object.id}
                )
            )


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class CarCreateView(
    LoginRequiredMixin,
    CreateCarForm,
    generic.CreateView
):
    model = Car
    fields = ["manufacturer", "model"]
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(
    LoginRequiredMixin,
    UpdateCarForm,
    generic.UpdateView
):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_form.html"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except Exception:
            return HttpResponseRedirect(
                reverse("taxi:car-delete", kwargs={"pk": self.object.id})
            )


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
