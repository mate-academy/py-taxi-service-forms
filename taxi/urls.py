from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CreateCarView,
    UpdateCarView,
    DeleteCarView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CreateManufacturerView,
    UpdateManufacturerView,
    DeleteManufacturerView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "manufacturers/create/",
        CreateManufacturerView.as_view(),
        name="create-manufacturer"
    ),
    path(
        "manufacturers/update/<int:pk>/",
        UpdateManufacturerView.as_view(),
        name="update-manufacturer"
    ),
    path(
        "manufacturers/delete/<int:pk>/",
        DeleteManufacturerView.as_view(),
        name="delete-manufacturer"
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "cars/create/",
        CreateCarView.as_view(),
        name="create-car"
    ),
    path(
        "cars/update/<int:pk>/",
        UpdateCarView.as_view(),
        name="update-car"
    ),
    path(
        "cars/delete/<int:pk>/",
        DeleteCarView.as_view(),
        name="delete-car"
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    )
]

app_name = "taxi"
