from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    # Основний додаток
    path("", include(("taxi.urls", "taxi"), namespace="taxi")),

    # Вбудована авторизація Django
    path("accounts/", include("django.contrib.auth.urls")),
]

# Debug toolbar — тільки якщо встановлений
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

# Статичні файли (для DEV)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
