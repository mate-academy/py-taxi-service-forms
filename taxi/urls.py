from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    car_create_view,
    car_update_view,
    car_delete_view,
    manufacturer_create_view,
    manufacturer_delete_view,
    manufacturer_update_view,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        manufacturer_create_view,
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        manufacturer_update_view,
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        manufacturer_delete_view,
        name="manufacturer-delete"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", car_create_view, name="car-create"),
    path("cars/<int:pk>/update/", car_update_view, name="car-update"),
    path("cars/<int:pk>/delete/", car_delete_view, name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
