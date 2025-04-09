from django.urls import path
from taxi import views
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

    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/create/", views.car_create, name="car-create"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/<int:pk>/edit/", views.car_update, name="car-update"),

    path("cars/<int:pk>/delete/", views.car_delete, name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),

    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        views.manufacturer_create,
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/edit/",
        views.manufacturer_update,
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        views.manufacturer_delete,
        name="manufacturer-delete"
    ),
]

app_name = "taxi"
