from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarAddView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerAddView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers-list/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturer-create/",
        ManufacturerAddView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "<int:pk>/manufacturer-update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "<int:pk>/manufacturer-delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),

    path("cars-list/", CarListView.as_view(), name="car-list"),
    path("cars-list/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("car-create/", CarAddView.as_view(), name="car-create"),
    path("<int:pk>/car-update/", CarUpdateView.as_view(), name="car-update"),
    path("<int:pk>/car-delete/", CarDeleteView.as_view(), name="car-delete"),

    path("drivers-list/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers-list/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
