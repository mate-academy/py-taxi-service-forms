from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("taxi.urls", namespace="taxi")),
    path("registration/", include("django.contrib.auth.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
]
