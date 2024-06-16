from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Driver, Car, Manufacturer
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from taxi.forms import RegistrationForm, UserLoginForm, UserPasswordResetForm, UserSetPasswordForm, \
    UserPasswordChangeForm
from django.contrib.auth import logout


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    cars = Car.objects.all()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
        "cars": cars,
    }

    return render(request, "pages/index.html", context=context)


def about_us(request):
    return render(request, 'pages/about-us.html')


def contact_us(request):
    return render(request, 'pages/contact-us.html')


def author(request):
    return render(request, 'pages/author.html')


# class ManufacturerListView(LoginRequiredMixin, generic.ListView):
#     model = Manufacturer
#     context_object_name = "manufacturer_list"
#     template_name = "taxi/manufacturer_list.html"
#     paginate_by = 5
#
#
# class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Manufacturer
#     fields = "__all__"
#     success_url = reverse_lazy("taxi:manufacturer-list")
#     template_name = "taxi/manufacturer_form.html"
#
#
# class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Manufacturer
#     fields = "__all__"
#     success_url = reverse_lazy("taxi:manufacturer-list")
#     template_name = "taxi/manufacturer_form.html"
#
#
# class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Manufacturer
#     success_url = reverse_lazy("taxi:manufacturer-list")
#     template_name = "taxi/manufacturer_confirm_delete.html"


# class CarListView(LoginRequiredMixin, generic.ListView):
#     model = Car
#     paginate_by = 5
#     queryset = Car.objects.all().select_related("manufacturer")


# class CarCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Car
#     fields = "__all__"
#     success_url = reverse_lazy("taxi:car-list")
#     template_name = "taxi/car_form.html"
#
#
# class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Car
#     fields = "__all__"
#     success_url = reverse_lazy("taxi:car-list")
#     template_name = "taxi/car_form.html"
#
#
# class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Car
#     success_url = reverse_lazy("taxi:car-list")
#     template_name = "taxi/car_confirm_delete.html"
#
#
# class CarDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Car
#
#
# class DriverListView(LoginRequiredMixin, generic.ListView):
#     model = Driver
#     paginate_by = 5
#
#
# class DriverDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Driver
#     queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


# Authentication

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully!")
            return redirect('/accounts/login')
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/sign-up.html', context)


class UserLoginView(LoginView):
    template_name = 'accounts/sign-in.html'
    form_class = UserLoginForm


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = UserSetPasswordForm


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = UserPasswordChangeForm


# Sections
def presentation(request):
    return render(request, 'sections/presentation.html')


def page_header(request):
    return render(request, 'sections/page-sections/hero-sections.html')


def features(request):
    return render(request, 'sections/page-sections/features.html')


def navbars(request):
    return render(request, 'sections/navigation/navbars.html')


def nav_tabs(request):
    return render(request, 'sections/navigation/nav-tabs.html')


def pagination(request):
    return render(request, 'sections/navigation/pagination.html')


def inputs(request):
    return render(request, 'sections/input-areas/inputs.html')


def forms(request):
    return render(request, 'sections/input-areas/forms.html')


def avatars(request):
    return render(request, 'sections/elements/avatars.html')


def badges(request):
    return render(request, 'sections/elements/badges.html')


def breadcrumbs(request):
    return render(request, 'sections/elements/breadcrumbs.html')


def buttons(request):
    return render(request, 'sections/elements/buttons.html')


def dropdowns(request):
    return render(request, 'sections/elements/dropdowns.html')


def progress_bars(request):
    return render(request, 'sections/elements/progress-bars.html')


def toggles(request):
    return render(request, 'sections/elements/toggles.html')


def typography(request):
    return render(request, 'sections/elements/typography.html')


def alerts(request):
    return render(request, 'sections/attention-catchers/alerts.html')


def modals(request):
    return render(request, 'sections/attention-catchers/modals.html')


def tooltips(request):
    return render(request, 'sections/attention-catchers/tooltips-popovers.html')
