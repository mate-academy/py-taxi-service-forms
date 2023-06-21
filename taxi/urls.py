from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CreateCarView,
    UpdateCarView,
    DeleteCarView,
    CreateManufacturerView,
    UpdateManufacturerView,
    DeleteManufacturerView,
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
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("car/create/", CreateCarView.as_view(), name="car-create"),
    path("car/<int:pk>/update/", UpdateCarView.as_view(), name="car-update"),
    path("car/<int:pk>/delete/", DeleteCarView.as_view(), name="car-delete"),
    path(
        "manufacturer/create/",
        CreateManufacturerView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturer/<int:pk>/update/",
        UpdateManufacturerView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturer/<int:pk>/delete/",
        DeleteManufacturerView.as_view(),
        name="manufacturer-delete",
    ),
]

app_name = "taxi"
