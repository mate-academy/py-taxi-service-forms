from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "manufacturers/",
        views.ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        views.ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/update/<int:pk>/",
        views.ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/delete/<int:pk>",
        views.ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
    path("cars/", views.CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", views.CarCreateView.as_view(), name="car-create"),
    path(
        "cars/update/<int:pk>/",
        views.CarUpdateView.as_view(),
        name="car-update"
    ),
    path(
        "cars/delete/<int:pk>",
        views.CarDeleteView.as_view(),
        name="car-delete"
    ),
    path("drivers/", views.DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        views.DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
