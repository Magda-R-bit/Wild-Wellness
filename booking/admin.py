from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name', 'check_in', 'check_out', 'created_at')
    list_filter = ('check_in', 'check_out', 'created_at')
    search_fields = ('user_username', 'item_name')