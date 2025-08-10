from django.contrib import admin
from django.urls import path

from taxi.views import index, CarListView, CarDetailView, DriverListView, DriverDetailView, ManufacturerListView

urlpatterns = [
    path("", index, name="index"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("manufactures/", ManufacturerListView.as_view(), name="manufacturer-list"),
]

app_name = "taxi"