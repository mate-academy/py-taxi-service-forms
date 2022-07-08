from django.urls import path

from .views import index, CarListView, CarDetailView, DriverListView, DriverDetailView, ManufacturerListView, \
    CarCreateView, ManufacturerCreateView, CarUpdateView, CarDeleteView, ManufacturerUpdateView, ManufacturerDeleteView, \
    DriverCreateView, DriverDeleteView, LicenseUpdateView, set_user_to_car_view, delete_user_from_car_view

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturer/create/", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturer/update/<int:pk>", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturer/delete/<int:pk>", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/update/<int:pk>/", CarUpdateView.as_view(), name="car-update"),
    path("cars/delete/<int:pk>/", CarDeleteView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/create/", DriverCreateView.as_view(), name="driver-create"),
    path("drivers/delete/<int:pk>", DriverDeleteView.as_view(), name="driver-delete"),
    path("drivers/<int:pk>/update_license/", LicenseUpdateView.as_view(), name="license-update"),
    path("cars/<int:pk>/set_driver", set_user_to_car_view, name="set_driver"),
    path("cars/<int:pk>/delete_driver", delete_user_from_car_view, name="delete_driver"),
]

app_name = "taxi"
