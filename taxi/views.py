from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Driver, Car, Manufacturer

from .forms import CarForm, ManufacturerForm


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


def car_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": CarForm()
        }
        return render(request, "taxi/car_form.html", context=context)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = Car.objects.create(
                model=form.cleaned_data["model"],
                manufacturer=form.cleaned_data["manufacturer"]
            )
            car.drivers.set(form.cleaned_data["drivers"])
            return HttpResponseRedirect(reverse("taxi:car-list"))
        context = {
            "form": form
        }

    return render(request, "taxi/car_form.html", context=context)


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = ["model", "manufacturer", "drivers"]
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confrim_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    template_name = "taxi/car_confrim_delete.html"
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = ["name", "country"]
    success_url = reverse_lazy("taxi:manufacturer-list")


def manufacturer_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": ManufacturerForm()
        }
        return render(request, "taxi/manufacturer_form.html", context=context)

    if request.method == "POST":
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            (Manufacturer.objects.create
             (country=form.cleaned_data["country"],
              name=form.cleaned_data["name"]))
            return HttpResponseRedirect(reverse("taxi:manufacturer-list"))
        context = {
            "form": form
        }

    return render(request, "taxi/manufacturer_form.html", context=context)
