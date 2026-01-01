from django.urls import path, include


from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    DriverListView,
    DriverDetailView,
)

car_urls = [
    path("", CarListView.as_view(), name="car-list"),
    path("<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("create/", CarCreateView.as_view(), name="car-create"),
    path("<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
]

manufacturer_urls = [
    path("", ManufacturerListView.as_view(), name="manufacturer-list"),
    path(
        "create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
]

driver_urls = [
    path("", DriverListView.as_view(), name="driver-list"),
    path(
        "<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", include(manufacturer_urls)),
    path("cars/", include(car_urls)),
    path("drivers/", include(driver_urls)),
]

app_name = "taxi"
