from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cabin = self.get_object()

        if self.request.user.is_authenticated:
            # Show approved reviews + unapproved reviews
            # if they belong to the user
            context["reviews"] = cabin.reviews.filter(
                Q(approved=True) | Q(user=self.request.user)
            )
        else:
            # Show only approved reviews to logged-out users
            context["reviews"] = cabin.reviews.filter(approved=True)

        context["review_form"] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        cabin = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.cabin = cabin
            review.save()
            messages.success(
                request, "✅ Review has been posted successfully!"
            )
            return redirect("cabin_detail", pk=cabin.pk)

        context = self.get_context_data()
        context["review_form"] = form
        return self.render_to_response(context)


# Review List
class ReviewListView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "reviews/review_list.html"
    paginate_by = 5

    def get_queryset(self):
        cabin_id = self.kwargs["cabin_id"]
        return Review.objects.filter(cabin__id=cabin_id, approved=True)

    def get_context_data(self, **kwargs):
        """
        Adds the cabin object to the context.
        """
        context = super().get_context_data(**kwargs)
        context["cabin"] = get_object_or_404(Cabin, id=self.kwargs["cabin_id"])
        return context


# Create Review
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["review_form"] = ReviewForm()
        context["cabin"] = get_object_or_404(Cabin, id=self.kwargs["cabin_id"])
        print(f"DEBUG: Form is being passed: {context.get('form')}")
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cabin = get_object_or_404(
            Cabin, id=self.kwargs["cabin_id"]
        )
        messages.success(
            self.request, "✅ Your review has been successfully created!"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "cabin_detail", kwargs={"pk": self.object.cabin.id}
        )


# Update Review
class ReviewEditView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_form.html"

    def test_func(self):
        """
        Ensures that only the review owner can edit an unapproved review.
        """
        review = self.get_object()
        return self.request.user == review.user and not review.approved

    def form_valid(self, form):
        messages.success(self.request, "✅ Your review has been updated.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "cabin_detail", kwargs={"pk": self.object.cabin.id}
        )


# Delete Review
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"
    success_url = reverse_lazy("cabin_detail")

    def test_func(self):
        """
        Ensures that only the review owner can delete an unapproved review.
        """
        review = self.get_object()
        return self.request.user == review.user and not review.approved

    def get_success_url(self):
        return reverse_lazy(
            "cabin_detail", kwargs={"pk": self.object.cabin.pk}
        )

    def form_valid(self, form):
        """Handles the form submission (deletion) and success message."""
        messages.success(
            self.request, "✅ Your review has been successfully deleted!"
        )
        return super().form_valid(form)
