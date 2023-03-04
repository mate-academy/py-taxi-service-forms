from django.urls import path

from .views import (
    index,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    CarListView,
    CarUpdateView,
    CarDetailView,
    CarCreateView,
    CarDeleteView
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
    path(
        "car/create/",
        CarCreateView.as_view(),
        name="car-create"
    ),
    path(
        "car/<int:pk>/update/",
        CarUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "car/<int:pk>/delete/",
        CarDeleteView.as_view(),
        name="car-delete"
    ),
    path(
        "manufacturer/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturer/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturer/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
]

app_name = "taxi"
