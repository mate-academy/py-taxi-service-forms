from django.urls import path

from .views import index, CarListView, CarDetailView, DriverListView, \
    DriverDetailView, ManufacturerListView, CarCreateView, CarUpdateView, \
    CarDeleteView, ManufacturerCreateView, ManufacturerUpdateView, \
    ManufacturerDeleteView, DriverCreateView, DriverUpdateView, \
    DriverDeleteView, DriverUpdateLicenseView, set_driver_to_car_view, \
    delete_driver_from_cars_view

urlpatterns = [
    path("", index,
         name="index"),
    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("manufacturers/create/", ManufacturerCreateView.as_view(),
         name="manufacturer_create"),
    path("manufacturers/<int:pk>/update/", ManufacturerUpdateView.as_view(),
         name="manufacturer_update"),
    path("manufacturers/<int:pk>/delete/", ManufacturerDeleteView.as_view(),
         name="manufacturer_delete"),
    path("drivers/", DriverListView.as_view(),
         name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="driver-detail"),
    path("driver/create/", DriverCreateView.as_view(),
         name="driver_create"),
    path("driver/<int:pk>/update/", DriverUpdateView.as_view(),
         name="driver_update"),
    path("driver/<int:pk>/license_update/", DriverUpdateLicenseView.as_view(),
         name="license_update"),
    path("driver/<int:pk>/delete/", DriverDeleteView.as_view(),
         name="driver_delete"),
    path("cars/", CarListView.as_view(),
         name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(),
         name="car-detail"),
    path("cars/create/", CarCreateView.as_view(),
         name="car_create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(),
         name="car_update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(),
         name="car_delete"),
    path("cars/<int:pk>/set_driver/", set_driver_to_car_view,
         name="set_driver"),
    path("cars/<int:pk>/delete_driver_from_cars/",
         delete_driver_from_cars_view,
         name="delete_driver_from_cars"),

]

app_name = "taxi"
