from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),

    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturer-create/", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/<int:pk>/delete", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("manufacturers/<int:pk>/update", ManufacturerUpdateView.as_view(), name="manufacturer-update"),

    path("cars/", CarListView.as_view(), name="car-list"),
    path("car-create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/<int:pk>/delete", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/update", CarUpdateView.as_view(), name="car-update"),

    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("driver-create/", DriverCreateView.as_view(), name="driver-create"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("drivers/<int:pk>/delete", DriverDeleteView.as_view(), name="driver-delete"),
    path("drivers/<int:pk>/update/license-number", DriverUpdateView.as_view(), name="driver-update-license-number"),
]

app_name = "taxi"
