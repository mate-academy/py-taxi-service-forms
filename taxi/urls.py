from django.urls import path
from . import views

from .views import (
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

app_name = "taxi"

urlpatterns = [
path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturers/create/', ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturers/<int:pk>/update/', ManufacturerUpdateView.as_view(), name='manufacturer_update'),
    path('manufacturers/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer_delete'),
]

