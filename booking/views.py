from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm


# View to list all bookings of the current user
class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
    
    def get_template_names(self):
        print("Rendering template: booking/booking_list.html")
        return ["booking/booking_list.html"]
    


# View to create a new booking
class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')  # Redirect after success
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        response = super().form_valid(form)
        
        messages.success(self.request, 'Your booking has been successfully submitted!')
        messages.success(self.request, 'A confirmation email has been sent to your email address.')  # Show success message
    
        return response  # Automatically redirects after successful save
    

    
# View to update an existing booking
class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')  # Redirect after success

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)  # Allow only user bookings to be updated
    
    def form_valid(self, form):
        response = super().form_valid(form)
    
        messages.success(self.request, 'Your booking has been successfully updated!')
        return response

# View to delete a booking
class BookingDelete(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')  # Redirect after success

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)  # Allow only user bookings to be deleted
    
    def form_valid(self, form):
        response = super().form_valid(form)
    
        messages.success(self.request, 'Your booking has been successfully deleted!')
        return response

