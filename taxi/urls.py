from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    CarCreateView,
    CarDeleteView,
    CarUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/edit",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-edit",
    ),
    path(
        "manufacturers/<int:pk>/delete",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "cars/create",
        CarCreateView.as_view(),
        name="car-create",
    ),
    path(
        "cars/<int:pk>/edit",
        CarUpdateView.as_view(),
        name="car-edit",
    ),
    path(
        "cars/<int:pk>/delete",
        CarDeleteView.as_view(),
        name="car-delete",
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path("drivers/",
         DriverListView.as_view(),
         name="driver-list"
         ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
