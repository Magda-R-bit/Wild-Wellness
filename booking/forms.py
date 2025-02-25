from django import forms
from .models import Booking
from cabins.models import Cabin
import datetime


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['cabin', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': datetime.date.today().strftime('%Y-%m-%d')}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': datetime.date.today().strftime('%Y-%m-%d')}),
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['cabin'].queryset = Cabin.objects.filter(is_available=True)
        
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")
        today = datetime.date.today()

        # Check if check-in is in the past
        if check_in and check_in < today:
            raise forms.ValidationError("⚠️Check-in date cannot be in the past!")

        # Check if check-out is before check-in
        if check_out and check_in and check_out <= check_in:
            raise forms.ValidationError("⚠️Check-out date must be after check-in!")

        return cleaned_data

class AvailabilityForm(forms.Form):
    cabin = forms.ModelChoiceField(queryset=Cabin.objects.all(), required=True)
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    check_out = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get("check_in")
        check_out = cleaned_data.get("check_out")
        today = datetime.date.today()

        if check_in and check_in < today:
            raise forms.ValidationError("⚠️Check-in date cannot be in the past!")

        if check_out and check_in and check_out <= check_in:
            raise forms.ValidationError("⚠️Check-out date must be after check-in!")

        return cleaned_data