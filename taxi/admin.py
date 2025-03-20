from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("license_number",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "license_number",
                    )
                },
            ),
        )
    )

    @admin.display(description="Groups")
    def display_groups(self, obj: Driver) -> str:
        return ", ".join([group.name for group in obj.groups.all()]) or "-"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "display_drivers")
    search_fields = ("model", "manufacturer__name",)
    list_filter = ("model", "manufacturer",)
    ordering = ("model",)

    @admin.display(description="Drivers")
    def display_drivers(self, obj: Car) -> str:
        return ", ".join([driver.username for driver in obj.drivers.all()]) or "-"  # noqa :E501


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)
    ordering = ("name",)
