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
    ManufacturerDeleteView, CarCreateView, CarUpdateView, CarDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturers-create",
    ),

    path("manufacturers/update/<int:pk>/",
         ManufacturerUpdateView.as_view(),
         name="manufacturers-update"),

    path("manufacturers/delete/<int:pk>/",
         ManufacturerDeleteView.as_view(),
         name="manufacturers-delete"),

    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),

    path("cars/create/", CarCreateView.as_view(), name="cars-create"),
    path("cars/update/<int:pk>/", CarUpdateView.as_view(), name="cars-update"),
    path("cars/delete/<int:pk>/", CarDeleteView.as_view(), name="cars-delete"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
