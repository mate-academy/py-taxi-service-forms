from django.contrib import admin
from django.urls import path

from taxi.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "taxi"