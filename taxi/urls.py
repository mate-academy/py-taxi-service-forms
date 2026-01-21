from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreate,
    CarUpdate,
    CarDelete,
    ManufacturerCreate,
    ManufacturerUpdate,
    ManufacturerDelete,
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
        ManufacturerCreate.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdate.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDelete.as_view(),
        name="manufacturer-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarCreate.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdate.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDelete.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
