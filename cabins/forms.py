# forms.py
from django import forms
from .models import Review


RATING_CHOICES = [(i, f"{i}★") for i in range(1, 6)]


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(choices=RATING_CHOICES),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
