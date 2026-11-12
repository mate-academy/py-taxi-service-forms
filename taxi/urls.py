from django.urls import path
from django.views import View

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarViewCreate,
    CarViewUpdate,
    CarViewDelete,
    ManufacturerViewCreate,
    ManufacturerViewUpdate,
    ManufacturerViewDelete
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
        ManufacturerViewCreate.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerViewUpdate.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerViewDelete.as_view(),
        name="manufacturer-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarViewCreate.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarViewUpdate.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarViewDelete.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
