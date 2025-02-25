from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingList.as_view(), name='booking_list'),  # List bookings
    path('create/', views.BookingCreate.as_view(), name='booking_create'),  # Create a new booking
    path('booked-dates/', views.BookedDatesView.as_view(), name='booked_dates'),  # FullCalendar API
    path('availability/', views.CheckAvailabilityView.as_view(), name='check_availability'),  # Check availability
    path('update/<int:pk>/', views.BookingUpdate.as_view(), name='booking_update'),  # Update a booking
    path('delete/<int:pk>/', views.BookingDelete.as_view(), name='booking_delete'),  # Delete a booking
]
