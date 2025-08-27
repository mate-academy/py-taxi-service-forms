from django.core.exceptions import ImproperlyConfigured
from .base import *

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ImproperlyConfigured("DJANGO_SECRET_KEY env var is required")

ALLOWED_HOSTS = ["127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ["https://taxi-service-andriy125.onrender.com"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", ""),
        "USER": os.environ.get("POSTGRES_USER", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", ""),
        "PORT": int(os.environ.get("POSTGRES_DB_PORT", "")),
    }
}
