from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarFormatCreateView,
    CarFormatUpdateView,
    CarFormatDeleteView,
    ManufacturerFormatCreateView,
    ManufacturerFormatUpdateView,
    ManufacturerFormatDeleteView,
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
        ManufacturerFormatCreateView.as_view(),
        name="manufacturer-format-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerFormatUpdateView.as_view(),
        name="manufacturer-format-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerFormatDeleteView.as_view(),
        name="manufacturer-format-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path(
        "cars/create/",
        CarFormatCreateView.as_view(),
        name="car-format-create"
    ),
    path(
        "cars/<int:pk>/update/",
        CarFormatUpdateView.as_view(),
        name="car-format-update"
    ),
    path(
        "cars/<int:pk>/delete/",
        CarFormatDeleteView.as_view(),
        name="car-format-delete"
    ),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
