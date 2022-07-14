from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ManufacturerCreateView,
    DriverCreateView,
    DriverDeleteView,
    DriverUpdateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    assign_car_to_driver
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("cars/create", CarCreateView.as_view(), name="car-create"),
    path("cars/update/<int:pk>/", CarUpdateView.as_view(), name="car-update"),
    path("cars/delete/<int:pk>/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/assign", assign_car_to_driver, name="car-assign"),
    path("manufacturers/create", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/update/<int:pk>/", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/delete/<int:pk>/", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("drivers/create", DriverCreateView.as_view(), name="driver-create"),
    path("drivers/delete/<int:pk>/", DriverDeleteView.as_view(), name="driver-delete"),
    path("drivers/update/<int:pk>/", DriverUpdateView.as_view(), name="driver-update"),
]

app_name = "taxi"
