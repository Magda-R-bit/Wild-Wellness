from django.contrib import admin
from .models import Cabin, Review
from django.contrib import messages


@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "price_per_night",
        "is_available",
        "max_guests",
        "image",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "cabin", "rating", "created_at", "approved")
    list_filter = ("approved", "rating", "created_at")
    search_fields = ("user__username", "cabin__name")
    actions = ["approve_reviews"]

    def approve_reviews(self, request, queryset):
        count = 0
        for review in queryset:
            if not review.approved:
                review.approved = True
                review.save()
                count += 1

        self.message_user(
            request,
            f"{count} ✅ review successfully approved!",
            messages.SUCCESS,
        )

    approve_reviews.short_description = "Approve selected reviews"
