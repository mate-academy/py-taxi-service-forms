from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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
    template_name = "taxi/manufacturer_confirm_delete.html"
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


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
    template_name = "taxi/car_confirm_delete.html"
    success_url = reverse_lazy("taxi:car-list")


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


# def create_message_view(request: HttpRequest) -> HttpResponseRedirect:
#     context = {}
#     form = MessageForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("messager:message-list"))
#     context["form"] = form
#     return render(request, "messager/message_form.html", context=context)



    # if request.method == "GET":
    #     context1 = {
    #         "form": CarForm()
    #     }
    #     return render(request, "taxi/car_form.html", context=context1)
    # elif request.method == "POST":
    #     form = CarForm(request.POST)
    #
    #     if form.is_valid():
    #         Car.objects.create(**form.cleaned_data)
    #         return HttpResponseRedirect(reverse("taxi:car-list"))
    #     context2 = {
    #         "form": form
    #     }
    #     return render(request, "taxi/car_form.html", context=context2)


# def manufacturer_create_view(request: HttpRequest) -> HttpResponseRedirect:
#     context = {}
#     form = ManufacturerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("taxi:manufacturer-list"))
#     context["form"] = form
#     return render(request, "taxi/manufacturer_form.html", context=context)


    # if request.method == "GET":
    #     context1 = {
    #         "form": ManufacturerForm()
    #     }
    #     return render(request, "taxi/manufacturer_form.html", context=context1)
    # elif request.method == "POST":
    #     form = ManufacturerForm(request.POST)
    #
    #     if form.is_valid():
    #         Manufacturer.objects.create(**form.cleaned_data)
    #         return HttpResponseRedirect(reverse("taxi:manufacturer-list"))
    #     context2 = {
    #         "form": form
    #     }
    #     return render(request, "taxi/manufacturer_form.html", context=context2)

