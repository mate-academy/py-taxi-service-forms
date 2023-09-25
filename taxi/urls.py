from django.urls import path, include

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
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

cars_urlpatterns = [
    path("", CarListView.as_view(), name="car-list"),
    path("create/", CarCreateView.as_view(), name="car-create"),
    path(
        "<int:pk>/",
        include(
            [
                path("", CarDetailView.as_view(), name="car-detail"),
                path("update/", CarUpdateView.as_view(), name="car-update"),
                path("delete/", CarDeleteView.as_view(), name="car-delete"),
            ]
        ),
    ),
]

manufacturers_urlspatterns = [
    path(
        "",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "create/", ManufacturerCreateView.as_view(), name="manufacturer-create"
    ),
    path(
        "<int:pk>/",
        include(
            [
                path(
                    "update/",
                    ManufacturerUpdateView.as_view(),
                    name="manufacturer-update",
                ),
                path(
                    "delete/",
                    ManufacturerDeleteView.as_view(),
                    name="manufacturer-delete",
                ),
            ]
        ),
    ),
]

urlpatterns = [
    path("", index, name="index"),
    path("cars/", include(cars_urlpatterns)),
    path("manufacturers/", include(manufacturers_urlspatterns)),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
