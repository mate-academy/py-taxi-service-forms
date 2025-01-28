"""taxi_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from taxi.views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, ManufacturerListView, \
    ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("taxi.urls", namespace="taxi")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('manufacturers/create/', ManufacturerCreateView.as_view(), name='manufacturer-create'),
    path('manufacturers/<int:pk>/update/', ManufacturerUpdateView.as_view(), name='manufacturer-update'),
    path('manufacturers/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
