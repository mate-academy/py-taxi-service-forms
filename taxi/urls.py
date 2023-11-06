from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarCreateView,
    DriverCreateView,
    ManufacturerCreateView,
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
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("car/create/", CarCreateView.as_view(), name="car-create"),
    path("car/update/<int:pk>", CarUpdateView.as_view(), name="car-update"),
    path("car/delete/<int:pk>", CarDeleteView.as_view(), name="car-delete"),
    path("driver/create/", DriverCreateView.as_view(), name="driver-create"),
    path('manufacturer/create', ManufacturerCreateView.as_view(), name="manufacturer-create"),
]

app_name = "taxi"
