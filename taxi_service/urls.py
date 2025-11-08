from django.contrib import admin
from django.urls import path, include
from taxi.views import (
    CarListView,
    CarDetailView,
    ManufacturerListView,
    DriverListView,
    DriverDetailView,
    IndexView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", IndexView.as_view(), name="index"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail",
    ),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("taxi/", include("taxi.urls")),
]
