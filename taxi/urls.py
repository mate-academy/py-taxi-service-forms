from django.urls import path

from .views import index, CarListView, CarDetailView, DriverListView, DriverDetailView, ManufacturerListView, \
    ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView, CarCreateView, CarDeleteView, CarUpdateView, \
    DriverCreateView, DriverDeleteView, DriverUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturers/manufacturer_create/", ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path("manufacturers/manufacturer_update/<int:pk>/", ManufacturerUpdateView.as_view(), name='manufacturer-update'),
    path("manufacturers/manufacturer_delete/<int:pk>/", ManufacturerDeleteView.as_view(), name='manufacturer-delete'),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/car_create/", CarCreateView.as_view(), name='car-create'),
    path("cars/car_delete/<int:pk>/", CarDeleteView.as_view(), name='car-delete'),
    path("cars/car_update/<int:pk>/", CarUpdateView.as_view(), name='car-update'),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/driver_create/", DriverCreateView.as_view(), name='driver-create'),
    path("drivers/driver_update/<int:pk>/", DriverUpdateView.as_view(), name='driver-update'),
    path("drivers/driver_delete/<int:pk>/", DriverDeleteView.as_view(), name='driver-delete'),
]

app_name = "taxi"
