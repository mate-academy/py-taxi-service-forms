from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ManufacturersCreateView,
    ManufacturersUpdateView,
    ManufacturersDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    # manufacturer paths
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("manufacturer/create/",
         ManufacturersCreateView.as_view(),
         name="manufacturer-create"),
    path("manufacturer/<int:pk>/update/",
         ManufacturersUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturer/<int:pk>/delete/",
         ManufacturersDeleteView.as_view(),
         name="manufacturer-delete"),


    # Car paths
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),

    # driver paths
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
