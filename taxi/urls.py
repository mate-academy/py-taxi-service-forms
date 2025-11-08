from django.urls import path
from taxi.views import (
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

app_name = "taxi"

urlpatterns = [
    path(
        "cars/create/",
        CarCreateView.as_view(),
        name="car-create",
    ),
    path(
        "cars/<int:pk>/update/",
        CarUpdateView.as_view(),
        name="car-update",
    ),
    path(
        "cars/<int:pk>/delete/",
        CarDeleteView.as_view(),
        name="car-delete",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
]
