from django.urls import path

from .views import (index, CarListView, CarDetailView, DriverListView, DriverDetailView, ManufacturerListView,
                    DriverCreateView, DriverDeleteView, ManufacturerCreateView, ManufacturerUpdateView,
                    ManufacturerDeleteView, CarsCreateView, CarsUpdateView, CarsDeleteView, DriverUpdateView,
                    assign_to_car)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListView.as_view(),
         name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(),
         name="car-detail"),
    path("drivers/", DriverListView.as_view(),
         name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="driver-detail"),
    path("drivers/create", DriverCreateView.as_view(),
         name="driver-create"),
    path("drivers/<int:pk>/delete", DriverDeleteView.as_view(),
         name="driver-delete"),
    path("drivers/<int:pk>/update", DriverUpdateView.as_view(),
         name="driver-update"),
    path("manufacturers/create", ManufacturerCreateView.as_view(),
         name="manufacturer-create"),
    path("manufacturers/<int:pk>/update", ManufacturerUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete", ManufacturerDeleteView.as_view(),
         name="manufacturer-delete"),
    path("cars/create", CarsCreateView.as_view(),
         name="car-create"),
    path("cars/<int:pk>/update", CarsUpdateView.as_view(),
         name="cars-update"),
    path("cars/<int:pk>/delete", CarsDeleteView.as_view(),
         name="cars-delete"),
    path("cars/<int:pk>/<operation>/", assign_to_car,
         name="car-assign"),
]

app_name = "taxi"
