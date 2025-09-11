from django.contrib import admin
from django.urls import path

from taxi.views import (index,
                        CarListView,
                        CarDetailView,
                        DriverListView,
                        DriverDetailView,
                        ManufacturerListView,
                        test_session_view, CustomerCreateView,
                        CustomerListView, CarCreateView,
                        CarUpdateView, CarDeleteView,
                        ManufacturerCreateView,
                        ManufacturerUpdateView,
                        ManufacturerDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
    path("test-session/", test_session_view, name="test-session"),
    path(
        "customer/create/",
        CustomerCreateView.as_view(),
        name="customer-create"
    ),
    path("customers/", CustomerListView.as_view(), name="customer-list"),
]

app_name = "taxi"
