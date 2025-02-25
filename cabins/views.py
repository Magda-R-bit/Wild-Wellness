from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from .models import Cabin, Review
from .forms import ReviewForm


class CabinsListView(ListView):
    model = Cabin
    template_name = "cabins/cabins_list.html"
    context_object_name = "cabins"


class CabinDetail(DetailView):
    model = Cabin
    template_name = "cabins/cabin_detail.html"
    context_object_name = "cabin"


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    context_object_name = "reviews"
    
    def get_queryset(self):
        cabin_id = self.kwargs["cabin_id"]
        if self.request.user.is_authenticated:
            return Review.objects.filter(cabin=cabin_id).filter(models.Q(approved=True) | models.Q(user=self.request.user))
        return Review.objects.filter(cabin=cabin_id).filter(approved=True)
    

class ReviewCreateAJAXView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
   
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cabin = get_object_or_404(Cabin, id=self.kwargs["cabin_id"])
        review = form.save()
       
        return JsonResponse({
            "user": review.user.username,
            "rating": review.rating,
            "comment": review.comment,
            "created": review.created_at.strftime("%Y-%m-%D, %H:%M"),
            "approved": review.approved,
       })
        

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"
    
    
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
    
    def form_valid(self, form):
        messages.success(self.request, "✅ Review updated successfully!")
        return super().form_valid(form)
    

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"
    success_url = reverse_lazy("cabin_list")
    
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "✅ Review deleted successfully!")
        return super().delete(request, *args, **kwargs)
    
    