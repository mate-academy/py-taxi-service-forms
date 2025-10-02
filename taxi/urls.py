from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerDeleteView,
    ManufacturerUpdateView,
    ManufacturerDetailView,
    CarCreateView,
    CarUpdateView,
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
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "manufacturer/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create-form"
    ),
    path(
        "manufacturer/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update-form"
    ),
    path(
        "manufacturer/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete-form"
    ),
    path(
        "manufacturer/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail"
    ),
    path(
        "cars/create/",
        CarCreateView.as_view(),
        name="car-create-form"
    ),
    path(
        "cars/<int:pk>/update/",
        CarUpdateView.as_view(),
        name="car-update-form"
    ),
    path(
        "cars/<int:pk>/delete/",
        CarDeleteView.as_view(),
        name="car-delete-form"
    )
]

app_name = "taxi"
