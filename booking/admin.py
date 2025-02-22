from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'total_price', 'created_at')
    list_filter = ('check_in', 'check_out', 'created_at')
    search_fields = ('user__username', 'check_in', 'check_out')
    date_hierarchy = 'created_at'

