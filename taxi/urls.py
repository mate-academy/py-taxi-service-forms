from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarFormatCreateView,
    CarFormatUpdateView,
    CarFormatDeleteView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerDetailView,
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
        "manufacturers/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail"
    ),
    path(
        "manufacturers/create/",
        ManufacturerFormatCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerFormatUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerFormatDeleteView.as_view(),
        name="manufacturer-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path(
        "cars/<int:pk>/update/",
        CarFormatUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars/<int:pk>/delete/",
        CarFormatDeleteView.as_view(),
        name="car-delete"
    ),
    path("cars/create/", CarFormatCreateView.as_view(), name="car-create"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
