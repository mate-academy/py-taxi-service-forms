from django.urls import path
from . import views

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
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
    path("cars/create/", views.CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", views.CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", views.CarDeleteView.as_view(), name="car-delete"),
    path("manufacturers/create/", views.ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/<int:pk>/update/", views.ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete/", views.ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
]

app_name = "taxi"
