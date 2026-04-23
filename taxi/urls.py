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
    path(
        "manufacturers-create/",
        CreateManufacturerView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturer-update/<int:pk>/",
        UpdateManufacturerView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturer-delete/<int:pk>/",
        DeleteManufacturerView.as_view(),
        name="manufacturer-delete"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("car-create/", CreateCarView.as_view(), name="car-create"),
    path("car-update/<int:pk>/", UpdateCarView.as_view(), name="car-update"),
    path("car-delete/<int:pk>/", DeleteCarView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
