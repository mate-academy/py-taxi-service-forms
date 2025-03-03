from django.urls import path, include

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreateView, CarDeleteView, CarUpdateView,
    ManufacturerCreateView, ManufacturerDeleteView,
    ManufacturerUpdateView
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
    path("", include("customers.urls", namespace="customers")),
    path("car/create/", CarCreateView.as_view(), name="car-create"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("manufacturers/create/", ManufacturerCreateView.as_view(),
         name="manufacturers-create"),
    path("manufacturers/<int:pk>/delete/", ManufacturerDeleteView.as_view(),
         name="manufacturers-delete"),
    path("camanufacturersr/<int:pk>/update/", ManufacturerUpdateView.as_view(),
         name="manufacturers-update"),
]

app_name = "taxi"
