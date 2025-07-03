from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView, CarCreateView, CarUpdateView, ManufacturerCreateView, ManufacturerUpdateView,
    ManufacturerDeleteView, CarDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("manufacturers/create/", ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/update/<int:pk>/", ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/dlete/<int:pk>/", ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/craete/", CarCreateView.as_view(), name="car-create"),
    path("cars/update/<int:pk>/", CarUpdateView.as_view(), name="car-update"),
    path("cars/delete/<int:pk>/", CarDeleteView.as_view(), name="car-delete"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),

]

app_name = "taxi"
