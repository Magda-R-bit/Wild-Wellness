from django import forms
from .models import Booking
from cabins.models import Cabin
import datetime
from datetime import date


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["cabin", "check_in", "check_out"]
        widgets = {
            "check_in": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "min": datetime.date.today().strftime("%Y-%m-%d"),
                }
            ),
            "check_out": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "min": datetime.date.today().strftime("%Y-%m-%d"),
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields["cabin"].queryset = Cabin.objects.filter(is_available=True)

    def clean(self):
        cleaned_data = super().clean()
        cabin = cleaned_data.get("cabin")
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")

        # Validation 1: Check-in date cannot be in the past
        if check_in and check_in < date.today():
            raise forms.ValidationError(
                "⚠️ Check-in date cannot be in the past!"
            )

        # Validation 2: Check-out date must be after check-in
        if check_in and check_out and check_out <= check_in:
            raise forms.ValidationError(
                "⚠️ Check-out date must be after check-in."
            )

        # Validation 3: Check for overlapping bookings
        if cabin and check_in and check_out:
            overlapping_booking = Booking.objects.filter(
                cabin=cabin,
                check_in__lt=check_out,  # Check if check-in overlaps
                check_out__gt=check_in,  # Check if check-out overlaps
            )

            if self.instance.pk:
                overlapping_booking = overlapping_booking.exclude(
                    pk=self.instance.pk
                )

            if overlapping_booking.exists():
                raise forms.ValidationError(
                    "❌ This cabin is already booked for the selected dates!"
                )

        return cleaned_data


class AvailabilityForm(forms.Form):
    cabin = forms.ModelChoiceField(queryset=Cabin.objects.all(), required=True)
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )
    check_out = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")
        today = datetime.date.today()

        if check_in and check_in < today:
            raise forms.ValidationError(
                "⚠️ Check-in date cannot be in the past!"
            )

        if check_out and check_in and check_out <= check_in:
            raise forms.ValidationError(
                "⚠️ Check-out date must be after check-in!"
            )

        return cleaned_data
