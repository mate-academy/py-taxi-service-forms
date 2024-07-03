from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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


class CustomModelFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field_name, field in form.fields.items():
            field.widget.attrs.update({"class": "form-control"})
        return form


class DeleteDialogMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_verbose_name"] = self.model._meta.verbose_name
        return context


class CarCreateView(
    LoginRequiredMixin,
    CustomModelFormMixin,
    generic.CreateView
):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_from.html"


class CarUpdateView(
    LoginRequiredMixin,
    CustomModelFormMixin,
    generic.UpdateView
):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_from.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "update"
        return context


class CarDeleteView(LoginRequiredMixin, DeleteDialogMixin, generic.DeleteView):
    model = Car
    template_name = "taxi/delete_record.html"
    success_url = reverse_lazy("taxi:car-list")


class ManufacturerCreateView(
    LoginRequiredMixin,
    CustomModelFormMixin,
    generic.CreateView
):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_form.html"


class ManufacturerUpdateView(
    LoginRequiredMixin,
    CustomModelFormMixin,
    generic.UpdateView
):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "update"
        return context


class ManufacturerDeleteView(
    LoginRequiredMixin,
    DeleteDialogMixin,
    generic.DeleteView
):
    model = Manufacturer
    template_name = "taxi/delete_record.html"
    success_url = reverse_lazy("taxi:manufacturer-list")
