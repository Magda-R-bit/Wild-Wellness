from django.contrib import admin
from .models import Cabin


@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "price_per_night", "is_available", "max_guests", "image")
