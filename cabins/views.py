from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, ListView, CreateView, UpdateView, DeleteView
import json
from django.http import JsonResponse
from django.db.models import Q
from .models import Cabin, Review
from django.views.decorators.csrf import csrf_exempt



class CabinsListView(ListView):
    model = Cabin
    template_name = "cabins/cabins_list.html"
    context_object_name = "cabins"


class CabinDetail(DetailView):
    model = Cabin
    template_name = "cabins/cabin_detail.html"
    context_object_name = "cabin"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(cabin=self.object, approved=True)
        return context

    
# Review List
class ReviewListView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "reviews/review_list.html"

    def get_queryset(self):
        """Get all approved reviews for a specific cabin"""
        cabin = get_object_or_404(Cabin, id=self.kwargs["cabin_id"])
        return Review.objects.filter(cabin=cabin, approved=True).order_by("-created_at")

    def render_to_response(self, context, **response_kwargs):
        """Return JSON if it's an AJAX request, otherwise return HTML"""
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            reviews = [
                {
                    "id": review.id,
                    "user": review.user.username,
                    "rating": review.rating,
                    "comment": review.comment,
                    "approved": review.approved,
                }
                for review in context["reviews"]
            ]
            return JsonResponse({"reviews": reviews})
        return super().render_to_response(context, **response_kwargs)
    
# Create Review
class ReviewCreateAJAXView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ["rating", "comment"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cabin = get_object_or_404(Cabin, id=self.kwargs["cabin_id"])
        review = form.save()

        return JsonResponse({
            "id": review.id,
            "user": review.user.username,
            "rating": review.rating,
            "comment": review.comment,
            "approved": review.approved,
        })

    def form_invalid(self, form):
        return JsonResponse({"error": "Invalid data"}, status=400)


# Update Review
class ReviewEditAJAXView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ["comment"]
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        if self.object.user != request.user:
            return JsonResponse({"error": "Unauthorized"}, status=403)

        data = json.loads(request.body)
        self.object.comment = data.get("comment", self.object.comment)
        self.object.save()

        return JsonResponse({"comment": self.object.comment})


# Delete Review
class ReviewDeleteAJAXView(LoginRequiredMixin, DeleteView):
    model = Review
    http_method_names = ["delete"]

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user != request.user:
            return JsonResponse({"error": "Unauthorized"}, status=403)

        self.object.delete()
        return JsonResponse({"success": True})
