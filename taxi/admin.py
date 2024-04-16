from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Driver, Car, Manufacturer


class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = (UserAdmin.fieldsets
                 + (("Additional info", {"fields": ("license_number",)}),))
    for_flake = ("first_name", "last_name", "license_number",)
    add_fieldsets = (UserAdmin.add_fieldsets
                     + (("Additional info",
                         {"fields": for_flake}),))


class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
