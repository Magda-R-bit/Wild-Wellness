from datetime import date
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['item_name', 'check_in', 'check_out',]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        if check_in and check_in < date.today():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        if check_in and check_out and check_in >= check_out:
            raise forms.ValidationError("Check out date must be after the check-in date.")
        return cleaned_data