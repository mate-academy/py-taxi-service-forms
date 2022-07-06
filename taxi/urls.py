from django.urls import path

from .views import (index, CarListView, CarDetailView, DriverListView,
                    DriverDetailView, ManufacturerListView, CarCreateView,
                    CarUpdateView,
                    CarDeleteView, ManufacturerCreateView,
                    ManufacturerUpdateView,
                    ManufacturerDeleteView, DriverCreateView, DriverDeleteView,
                    LicenseUpdateView, add_to_driver)

urlpatterns = [
    path(
        "", index, name="index"
    ),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
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
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "create-car/",
        CarCreateView.as_view(),
        name="create-car"
    ),
    path(
        "update-car/<int:pk>/",
        CarUpdateView.as_view(),
        name="update-car"
    ),
    path(
        "delete-car/<int:pk>/",
        CarDeleteView.as_view(),
        name="delete-car"
    ),
    path(
        "create-manufacturer/",
        ManufacturerCreateView.as_view(),
        name="create-manufacturer"
    ),
    path(
        "update-manufacturer/<int:pk>/",
        ManufacturerUpdateView.as_view(),
        name="update-manufacturer"
    ),
    path(
        "delete-manufacturer/<int:pk>/",
        ManufacturerDeleteView.as_view(),
        name="delete-manufacturer"
    ),
    path(
        "create-driver/",
        DriverCreateView.as_view(),
        name="create-driver"
    ),
    path(
        "delete-driver/<int:pk>/",
        DriverDeleteView.as_view(),
        name="delete-driver"
    ),
    path(
        "update-license/<int:pk>/",
        LicenseUpdateView.as_view(),
        name="update-license"
    ),
    path(
        "driver/<int:pk>/<action>/",
        add_to_driver,
        name="add-to-driver"
    ),

]

app_name = "taxi"
