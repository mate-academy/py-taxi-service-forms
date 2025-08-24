from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Driver, Car, Manufacturer
from .forms import ManufacturerForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
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


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_create.html"
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    template_name = "taxi/car_create.html"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    template_name = "taxi/car-delete.html"
    success_url = reverse_lazy("taxi:car-list")


# Funkcje do Manufacturer CRUD

@login_required
def manufacturer_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("taxi:manufacturer-list")
    else:
        form = ManufacturerForm()
    return render(request, "taxi/manufacturer_create.html", {"form": form})


@login_required
def manufacturer_update_view(request: HttpRequest, pk: int) -> HttpResponse:
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    if request.method == "POST":
        form = ManufacturerForm(request.POST, instance=manufacturer)
        if form.is_valid():
            form.save()
            return redirect("taxi:manufacturer-list")
    else:
        form = ManufacturerForm(instance=manufacturer)
    return render(request, "taxi/manufacturer_update.html", {"form": form})


@login_required
def manufacturer_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    if request.method == "POST":
        manufacturer.delete()
        return redirect("taxi:manufacturer-list")
    return render(
        request,
        "taxi/manufacturer_delete.html",
        {"manufacturer": manufacturer},
    )
