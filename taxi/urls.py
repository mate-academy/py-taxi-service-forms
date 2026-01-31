from django.contrib.auth import views as auth_views
from django.urls import path

from taxi.views import (
    CarCreateView,
    CarDeleteView,
    CarDetailView,
    CarListView,
    CarUpdateView,
    DriverDetailView,
    DriverListView,
    ManufacturerCreateView,
    ManufacturerDeleteView,
    ManufacturerListView,
    ManufacturerUpdateView,
    index,
)

app_name = "taxi"

urlpatterns = [
    path("", index, name="index"),
    path("accounts/login/", auth_views.LoginView.as_view(),
         name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(),
         name="logout"),

    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),

    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(),
         name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(),
         name="car-delete"),

    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="driver-detail"),
]
