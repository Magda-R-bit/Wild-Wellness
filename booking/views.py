from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    View,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http import JsonResponse
import datetime
from .models import Booking
from .forms import AvailabilityForm, BookingForm


# View to list all bookings of the current user
class BookingList(LoginRequiredMixin, ListView):
    model = Booking
    template_name = "booking/booking_list.html"
    context_object_name = "bookings"

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def get_template_names(self):
        print("Rendering template: booking/booking_list.html")
        return ["booking/booking_list.html"]


# View to create a new booking
class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking_list")  # Redirect after success

    def get_initial(self):
        """Pre-fill form if coming from availability page"""
        initial = super().get_initial()
        cabin_id = self.request.GET.get("cabin")
        check_in = self.request.GET.get("check_in")
        check_out = self.request.GET.get("check_out")

        if cabin_id:
            initial["cabin"] = cabin_id
        if check_in:
            initial["check_in"] = check_in
        if check_out:
            initial["check_out"] = check_out

        return initial

    def form_valid(self, form):
        cabin = form.cleaned_data["cabin"]
        check_in = form.cleaned_data["check_in"]
        check_out = form.cleaned_data["check_out"]

        # Check for overlapping bookings for the selected cabin and dates
        overlapping_booking = Booking.objects.filter(
            cabin=cabin,
            # Check if check-in date is before the checkout
            check_in__lt=check_out,
            # Check if checkout date is after the check-in
            check_out__gt=check_in
        ).exists()

        if overlapping_booking:
            # If there is an overlapping booking, show an error
            messages.error(
                self.request,
                "❌ This cabin is already booked for the selected dates!"
            )
            return self.form_invalid(form)

        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(
            self.request, "✅ Your booking has been successfully submitted!"
        )

        return response  # Automatically redirects after successful save


class BookedDatesView(View):
    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(check_in__gte=datetime.date.today())
        events = [
            {
                "title": f"Booked: {booking.cabin.name}",
                "start": str(booking.check_in),
                "end": str(booking.check_out),
                "color": "red",
            }
            for booking in bookings
        ]
        return JsonResponse(events, safe=False)


class CheckAvailabilityView(View):
    def get(self, request):
        form = AvailabilityForm(request.GET)
        available = None

        if form.is_valid():
            cabin = form.cleaned_data["cabin"]
            check_in = form.cleaned_data["check_in"]
            check_out = form.cleaned_data["check_out"]

            if check_in < datetime.date.today():
                return JsonResponse(
                    {"error": "⚠️ Check-in date cannot be in the past"},
                    status=400,
                )

            overlapping_bookings = Booking.objects.filter(
                cabin=cabin, check_in__lt=check_out, check_out__gt=check_in
            )

            available = not overlapping_bookings.exists()

        return render(
            request,
            "booking/availability.html",
            {"form": form, "available": available},
        )


# View to update an existing booking
class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking/booking_form.html"
    success_url = reverse_lazy("booking_list")  # Redirect after success

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user
        )  # Allow only user bookings to be updated

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request, "✅ Your booking has been successfully updated!"
        )
        return response


# View to delete a booking
class BookingDelete(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = "booking/booking_confirm_delete.html"
    success_url = reverse_lazy("booking_list")  # Redirect after success

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def form_valid(self, form):
        """Handles the form submission (deletion) and success message."""
        messages.success(
            self.request, "✅ Your booking has been successfully deleted!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        """Redirects after successful deletion."""
        return reverse_lazy("booking_list")
