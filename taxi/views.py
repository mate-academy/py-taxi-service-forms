from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import DriverForm, CarForm, \
    DriverLicenseUpdateForm, SearchForm
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


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 12
    queryset = Car.objects.all().select_related("manufacturer")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = SearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                model__icontains=form.cleaned_data["title"]
            )
        return self.queryset


class ManufacturerListView(CarListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    paginate_by = 3
    queryset = Manufacturer.objects.all()

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                Q(name__icontains=form.cleaned_data["title"]) |
                Q(country__icontains=form.cleaned_data["title"]))
        return self.queryset


class DriverListView(CarListView):
    model = Driver
    paginate_by = 12
    queryset = Driver.objects.all()

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                Q(username__icontains=form.cleaned_data["title"]) |
                Q(first_name__icontains=form.cleaned_data["title"]) |
                Q(last_name__icontains=form.cleaned_data["title"]) |
                Q(license_number__icontains=form.cleaned_data["title"]))
        return self.queryset


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


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car
    success_url = reverse_lazy("taxi:car-detail")


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("taxi:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("taxi:driver-list")


class DriverUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Driver
    form_class = DriverForm
    success_url = reverse_lazy("taxi:driver-list")


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Driver
    success_url = reverse_lazy("taxi:driver-list")


class DriverUpdateLicenseView(LoginRequiredMixin, generic.UpdateView):
    model = Driver
    form_class = DriverLicenseUpdateForm
    success_url = reverse_lazy("taxi:driver-list")


def set_driver_to_car_view(request, pk):
    car = Car.objects.get(pk=pk)
    car.drivers.add(request.user)
    return HttpResponseRedirect(reverse("taxi:car-detail", kwargs={"pk": pk}))


def delete_driver_from_cars_view(request, pk):
    car = Car.objects.get(pk=pk)
    car.drivers.remove(request.user)
    return HttpResponseRedirect(reverse("taxi:car-detail", kwargs={"pk": pk}))
