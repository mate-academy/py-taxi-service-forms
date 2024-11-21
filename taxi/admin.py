from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]
    ordering = ["manufacturer"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    ordering = ["name"]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    ordering = ["first_name", "last_name"]
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
