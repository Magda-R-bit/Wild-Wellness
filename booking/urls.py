from django.urls import path
from .views import BookingList, BookingCreate

urlpatterns = [
    path('list/', BookingList.as_view(), name='booking_list'),
    path('create/', BookingCreate.as_view(), name='booking_create'),
]

