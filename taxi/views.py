from http.client import HTTPResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from taxi.models import Driver, Manufacturer, Car, Customer


# Create your views here.
@login_required
def index(request):
    num_drivers = Driver.objects.all().count()
    num_manufacturers = Manufacturer.objects.all().count()
    num_cars = Car.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
        "num_visits": request.session['num_visits'],
    }
    return render(request, "taxi/index.html", context)

class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5

class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer").order_by("manufacturer__name")
    paginate_by = 5

class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car

class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5

class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")

def test_session_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "<h1>Test Session</h1>"
    )

class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("taxi:customer-list")
    template_name = "taxi/customer_form.html"

class CustomerListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    template_name = "taxi/customer_list.html"
    context_object_name = "customer_list"

class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_form.html"

class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_form.html"

class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_confirm_delete.html"

class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_form.html"


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_form.html"

class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_confirm_delete.html"