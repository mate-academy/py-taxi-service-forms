from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView, CarCreateView, ManufacturerCreateView, ManufacturerUpdateView, CarUpdateView,
    ManufacturerDeleteView, CarDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("manufacturers/create/", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("cars/update/<int:pk>/", CarUpdateView.as_view(), name="car-update"),
    path("manufacturers/<int:pk>/update/", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("manufacturers/<int:pk>/delete/", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
