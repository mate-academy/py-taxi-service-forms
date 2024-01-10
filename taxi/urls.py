from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarFormatListView,
    CarFormatCreateView,
    CarFormatUpdateView,
    CarFormatDeleteView,
    ManufacturerFormatCreateView,
    ManufacturerFormatUpdateView,
    ManufacturerFormatDeleteView,
    ManufacturerFormatListView,
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
        "cars-formats/",
        CarFormatListView.as_view(),
        name="car-format-list"),
    path(
        "cars-formats/create/",
        CarFormatCreateView.as_view(),
        name="car-create"
    ),
    path(
        "cars-formats/<int:pk>/update/",
        CarFormatUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars-formats/<int:pk>/delete/",
        CarFormatDeleteView.as_view(),
        name="car-delete"
    ),
    path(
        "manufacturers-formats/",
        ManufacturerFormatListView.as_view(),
        name="manufacturer-format-list"
    ),
    path(
        "manufacturers/create/",
        ManufacturerFormatCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerFormatUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerFormatDeleteView.as_view(),
        name="manufacturer-delete"
    ),
]

app_name = "taxi"
