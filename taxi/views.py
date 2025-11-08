from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Driver, Car, Manufacturer


class VerboseNameMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.verbose_name
        return context


class CancelUrlMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()

        try:
            context["cancel_url"] = obj.get_absolute_url()
        except AttributeError:
            model_name = obj._meta.model_name
            context["cancel_url"] = reverse(
                f"taxi:{model_name}-list")  # noqa: E231
        return context


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


class ManufacturerCreateView(
    VerboseNameMixin,
    LoginRequiredMixin,
    generic.CreateView
):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/form.html"


class ManufacturerUpdateView(
    VerboseNameMixin,
    LoginRequiredMixin,
    generic.UpdateView
):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/form.html"


class ManufacturerDeleteView(
    VerboseNameMixin,
    CancelUrlMixin,
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/confirm_delete.html"


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarCreateView(VerboseNameMixin, LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/form.html"


class CarUpdateView(VerboseNameMixin, LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/form.html"


class CarDeleteView(
    VerboseNameMixin,
    CancelUrlMixin,
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/confirm_delete.html"


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
