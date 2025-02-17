from django.urls import path
from .views import (
    index,
    ManufacturerListView, ManufacturerCreateView, ManufacturerUpdateView,
    ManufacturerDeleteView, CarListView, CarDetailView,
    CarCreateView, CarUpdateView, CarDeleteView,
    DriverListView, DriverDetailView, DriverUpdateView,
)

app_name = "taxi"

urlpatterns = [
    # Home Page
    path("", index, name="index"),

    # Manufacturer URLs
    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("manufacturers/new/", ManufacturerCreateView.as_view(),
         name="manufacturer-create"),
    path("manufacturers/<int:pk>/edit/", ManufacturerUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete/", ManufacturerDeleteView.as_view(),
         name="manufacturer-delete"),

    # Car URLs
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/new/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/edit/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),

    # Driver URLs
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="driver-detail"),
    path("drivers/<int:pk>/edit/", DriverUpdateView.as_view(),
         name="driver-update"),
]
