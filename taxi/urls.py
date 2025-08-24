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
    CarDeleteView, manufacturer_delete_view, manufacturer_update_view,
    manufacturer_create_view
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete", CarDeleteView.as_view(), name="car-delete"),
    path("manufacturer/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path(
        "manufacturer/create/",
        manufacturer_create_view,
        name="manufacturer-create"
    ),
    path(
        "manufacturer/<int:pk>/update/",
        manufacturer_update_view,
        name="manufacturer-update"
    ),
    path(
        "manufacturer/<int:pk>/delete/",
        manufacturer_delete_view,
        name="manufacturer-delete"
    ),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
