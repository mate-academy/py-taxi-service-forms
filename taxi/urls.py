from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarUpdateView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerUpdateView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/<int:pk>/update",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path(
        "cars/<int:pk>/update",
        CarUpdateView.as_view(),
        name="car-update",
    ),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    )
]

app_name = "taxi"
