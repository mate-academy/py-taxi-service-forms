from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
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


def car_create_view(request):
    context = {}
    form = CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("taxi:car-list")
    context["form"] = form
    return render(request, "taxi/car_form.html", context=context)


def car_update_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect("taxi:car-list")
    return render(request, "taxi/car_form.html", {"form": form})


def car_delete_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        car.delete()
        return redirect("taxi:car-list")
    return render(request, "taxi/car_confirm_delete.html", {"car": car})


def manufacturer_create_view(request):
    context = {}
    form = ManufacturerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("taxi:manufacturer-list")
    context["form"] = form
    return render(request, "taxi/manufacturer_form.html", context=context)


def manufacturer_update_view(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    form = ManufacturerForm(request.POST or None, instance=manufacturer)
    if form.is_valid():
        form.save()
        return redirect("taxi:manufacturer-list")
    return render(request, "taxi/manufacturer_form.html", {"form": form})


def manufacturer_delete_view(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    if request.method == "POST":
        manufacturer.delete()
        return redirect("taxi:manufacturer-list")
    return render(
        request,
        "taxi/manufacturer_confirm_delete.html",
        {"manufacturer": manufacturer}
    )
