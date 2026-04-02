from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    Car_Update_View,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    car_create_view,
    manufacturer_create_view,
    Manufacturer_Delete_View,
    ManufacturerUpdateView,
    Car_Delete_View

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
    path("cars/<int:pk>/update/",
         Car_Update_View.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/",
         Car_Delete_View.as_view(), name="car-delete"),
    path("drivers/",
         DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(), name="driver-detail"
    ),
    path("cars/create", car_create_view, name="car-create"),
    path("manufacturers/create", manufacturer_create_view,
         name="manufacturer-create"),
    path("manufacturers/<int:pk>/update/", ManufacturerUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete/", Manufacturer_Delete_View.as_view(),
         name="manufacturer-delete")
]

app_name = "taxi"
