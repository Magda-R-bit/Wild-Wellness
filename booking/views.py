from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from datetime import timedelta
from django.contrib import messages
from django.urls import reverse_lazy



class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    
class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')
    
    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        
        if booking.check_in and booking.check_out:
            days = (booking.check_out - booking.check_in).days
            price_per_night = 100  # Replace this with your dynamic logic if needed
            booking.total_price = days * price_per_night
            
        booking.save()
        
        
        messages.success(self.request, 'Your booking has been submitted!')
  
        return super().form_valid(form)