from django.urls import path

from taxi import views


urlpatterns = [
    path("", views.index, name="index"),
    path(
        "manufacturers/",
        views.ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", views.CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car-detail"),
    path("drivers/", views.DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        views.DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path("cars/create/", views.CarCreateView.as_view(), name="car-create"),
    path(
        "cars/<int:pk>/update/",
        views.CarUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars/<int:pk>/delete/",
        views.CarDeleteView.as_view(),
        name="car-delete"
    ),
    path(
        "manufacturers/create/",
        views.ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/",
        views.ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        views.ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
]

app_name = "taxi"
