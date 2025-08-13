from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerListCreateView,
    ManufacturerListUpdateView,
    ManufacturerListDeleteView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
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
        ManufacturerListCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerListUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerListDeleteView.as_view(),
        name="manufacturer-delete"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
