import os
import django
from django.conf import settings

def pytest_configure():
    if not settings.configured:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taxi_service.settings")
        django.setup()
