from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarFormCreate,
    ManufacturerFormCreate,
    CarFormUpdate,
    CarFormDelete,
    ManufacturerFormUpdate,
    ManufacturerFormDelete,
    DriverFormCreate
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
    path("drivers/create/", DriverFormCreate.as_view(), name="driver-create"),
    path("cars/create/", CarFormCreate.as_view(), name="car-create"),
    path("cars/<int:pk>/update", CarFormUpdate.as_view(), name="car-update"),
    path("cars/<int:pk>/delete", CarFormDelete.as_view(), name="car-delete"),
    path("manufacturers/create/", ManufacturerFormCreate.as_view(),
         name="manufacturer-create"
         ),
    path("manufacturers/<int:pk>/update", ManufacturerFormUpdate.as_view(),
         name="manufacturer-update"
         ),
    path("manufacturers/<int:pk>/delete", ManufacturerFormDelete.as_view(),
         name="manufacturer-delete"
         )


]

app_name = "taxi"
