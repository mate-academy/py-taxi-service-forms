from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from taxi.forms import ManufacturerForm
from taxi.models import Car, Driver, Manufacturer


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "taxi/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits

        context["num_cars"] = Car.objects.count()
        context["num_drivers"] = get_user_model().objects.count()
        context["num_manufacturers"] = Manufacturer.objects.count()
        context["num_visits"] = num_visits
        return context


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ManufacturerForm
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_form.html"

class ManufacturersListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    paginate_by = 5


class ManufacturerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Manufacturer

class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    success_url = reverse_lazy("taxi:manufacturer-list")

class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")

class CarCreateView(LoginRequiredMixin,generic.CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
class CarsListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        return self.model.objects.select_related("manufacturer")

class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car

class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")

class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")
class DriversListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver

    def get_queryset(self) -> QuerySet:
        return self.model.objects.prefetch_related("cars__manufacturer")


