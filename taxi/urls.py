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
    ManufacturerUpdateView, ManufacturerDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("manufacturers/manufacturer_create/",
         ManufacturerCreateView.as_view(),
         name="manufacturer-create"),
    path("manufacturers/<pk>/manufacturer_update/",
         ManufacturerUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturers/<pk>/manufacturer_delete/",
         ManufacturerDeleteView.as_view(),
         name="manufacturer-delete"),

    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/car_create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<pk>/car_update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<pk>/car_delete/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
