from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarListCreateView,
    CarListUpdateView,
    CarListDeleteView,
    ManufacturerListCreateView,
    ManufacturerListUpdateView,
    ManufacturerListDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
path("manufacturers/create/", ManufacturerListCreateView.as_view(), name="manufacturer-list-create"),
    path("manufacturers/<int:pk>/update/", ManufacturerListUpdateView.as_view(), name="manufacturer-list-update"),
    path("manufacturers/<int:pk>/delete/", ManufacturerListDeleteView.as_view(), name="manufacturer-list-delete"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarListCreateView.as_view(), name="car-list-create"),
    path("cars/<int:pk>/update/", CarListUpdateView.as_view(), name="car-list-update"),
    path("cars/<int:pk>/delete/", CarListDeleteView.as_view(), name="car-list-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
