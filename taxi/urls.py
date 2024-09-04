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
    ManufacturersDeleteView,
    ManufacturersUpdateView
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
    path("cars/create", CarsCreateView.as_view(), name="cars-create"),
    path("cars/<int:pk>/delete", CarsDeleteView.as_view(), name="cars-delete"),
    path("cars/<int:pk>/update", CarsUpdateView.as_view(), name="cars-update"),
    path(
        "manufacturers/create",
        ManufacturersCreateView.as_view(),
        name="manufacturers-create"
    ),
    path(
        "manufacturers/<int:pk>/delete",
        ManufacturersDeleteView.as_view(),
        name="manufacturers-delete"
    ),
    path(
        "manufacturers/<int:pk>/update",
        ManufacturersUpdateView.as_view(),
        name="manufacturers-update"
    ),

]

app_name = "taxi"
