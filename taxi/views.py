from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    DriverLicenceUpdateForm,
    CarForm,
    CarSearchForm,
    DriverSearchForm,
    DriverCreateForm,
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
    paginate_by = 10


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 10
    queryset = Car.objects.all().select_related("manufacturer")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)

        model = self.request.GET.get("model", "")

        context["search_form"] = CarSearchForm(initial={
            "model": model
        })

        return context

    def get_queryset(self):
        model = self.request.GET.get("model")

        if model:
            return self.queryset.filter(model__icontains=model)
        return self.queryset


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 10
    queryset = Driver.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DriverListView, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")

        context["search_form"] = DriverSearchForm(initial={
            "last_name": last_name
        })

        return context

    def get_queryset(self):
        last_name = self.request.GET.get("last_name")

        if last_name:
            return self.queryset.filter(last_name__icontains=last_name)
        return self.queryset


class DriverCreateView(generic.CreateView):
    model = Driver
    form_class = DriverCreateForm
    success_url = reverse_lazy("taxi:driver-list")


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverLicenceUpdateView(generic.UpdateView):
    model = Driver
    form_class = DriverLicenceUpdateForm
    template_name = "taxi/driver_licence_update.html"
    success_url = reverse_lazy("taxi:driver-list")


class DriverDeleteView(generic.DeleteView):
    model = Driver
    success_url = reverse_lazy("taxi:driver-list")


def driver_to_car(request, pk):
    current_car = Car.objects.get(pk=pk)
    if request.user in current_car.drivers.all():
        current_car.drivers.remove(request.user.id)
    else:
        current_car.drivers.add(request.user.id)
    current_car.save()

    return HttpResponseRedirect(reverse("taxi:car-detail", args=[pk]))
