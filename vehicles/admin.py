from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("id", "driver", "make", "model", "plate_number")
    list_filter = ("make", "model")
