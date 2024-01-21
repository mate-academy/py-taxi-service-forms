from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
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
    path("manufacturers-format/create/", ManufacturerCreateView.as_view(), name="manufacturer-create",),
    path("manufacturers-format/<int:pk>/update", ManufacturerUpdateView.as_view(), name="manufacturer-update",),
    path("manufacturers-format/<int:pk>/delete", ManufacturerDeleteView.as_view(), name="manufacturer-delete",),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars-format/create/", CarCreateView.as_view(), name="car-create"),
    path("cars-format/<int:pk>/update", CarUpdateView.as_view(), name="car-update"),
    path("cars-format/<int:pk>/delete", CarDeleteView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
