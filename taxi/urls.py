from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerFormCreateView,
    ManufacturerFormUpdateView,
    ManufacturerFormDeleteView,
    CarFormCreateView,
    CarFormUpdateView,
    CarFormDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerFormCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerFormUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerFormDeleteView.as_view(),
        name="manufacturer-delete"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create", CarFormCreateView.as_view(), name="car-create"),
    path(
        "cars/<int:pk>/update/",
        CarFormUpdateView.as_view(),
        name="car-update"),
    path(
        "cars/<int:pk>/delete/",
        CarFormDeleteView.as_view(),
        name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
