from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    DriverCreateView,
    DriverDeleteView,
    DriverUpdateView, ManufacturerCreateView, ManufacturerUpdateView,
    ManufacturerDeleteView
)


urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturers/create", ManufacturerCreateView.as_view(), name="manufacturer-form"),
    path("manufacturers/<int:pk>/update/", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("manufacturers/<int:pk>/delete/", ManufacturerUpdateView.as_view(), name="manufacturer-form"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-form"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-form"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/create", DriverCreateView.as_view(), name="driver-form"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/<int:pk>/update", DriverUpdateView.as_view(), name="driver-update"),
    path("drivers/<int:pk>/delete/", DriverDeleteView.as_view(), name="driver-delete"),

]

app_name = "taxi"
