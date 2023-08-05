from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarsCreateView,
    CarsUpdateView,
    CarsDeleteView,
    ManufacturersCreateView,
    ManufacturersUpdateView,
    ManufacturersDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("cars/create/", CarsCreateView.as_view(), name="car-create"),
    path(
        "cars/<int:pk>/update/",
        CarsUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars/<int:pk>/delete/",
        CarsDeleteView.as_view(),
        name="car-delete"
    ),
    path(
        "manufacturers/create/",
        ManufacturersCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturersUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturersDeleteView.as_view(),
        name="manufacturer-delete"
    ),
]

app_name = "taxi"
