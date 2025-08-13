from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CarForm, ManufacturerForm, ConfirmDeleteForm
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


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "taxi/car_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        context["form"] = ConfirmDeleteForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        return self.get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("taxi:car-list")


class ManufacturerCreateView(LoginRequiredMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Manufacturer
    template_name = "taxi/manufacturer_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["previous_url"] = self.request.META.get("HTTP_REFERER")
        context["form"] = ConfirmDeleteForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid():
            return super().post(request, *args, **kwargs)
        return self.get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("taxi:manufacturer-list")
