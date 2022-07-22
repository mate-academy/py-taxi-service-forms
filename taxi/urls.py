from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreateView,
    ManufacturerCreateView,
    CarUpdateView,
    ManufacturerUpdateView,
    CarDeleteView,
    ManufacturerDeleteView,
    DriverCreateView,
    DriverUpdateView,
    DriverDeleteView,
    DriverLicenseUpdateView,
    car_assign_driver,
    car_remove_driver
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturers/create", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/<int:pk>/update", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/<int:pk>/update", CarUpdateView.as_view(), name="car-update"),
    path("cars/create", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/delete", CarDeleteView.as_view(), name="car-delete"),
    path("cars/driver/<int:pk>/assign/", car_assign_driver,name="car-assign-driver"),
    path("cars/driver/<int:pk>/remove/",car_remove_driver,name="car-remove-driver"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/create", DriverCreateView.as_view(), name="driver-create"),
    path("drivers/<int:pk>/update", DriverUpdateView.as_view(), name="driver-update"),
    path("drivers/<int:pk>/delete", DriverDeleteView.as_view(), name="driver-delete"),
    path("drivers/<int:pk>/license-update", DriverLicenseUpdateView.as_view(), name="driver-license-update"),
]

app_name = "taxi"
