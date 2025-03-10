from django.urls import path
from .views import (
    CabinsListView,
    CabinDetail,
    ReviewListView,
    ReviewCreateView,
    ReviewEditView,
    ReviewDeleteView,
)


urlpatterns = [
    path("", CabinsListView.as_view(), name="cabins_list"),
    path("<int:pk>/", CabinDetail.as_view(), name="cabin_detail"),
    # Reviews
    path(
        "cabins/<int:cabin_id>/reviews/",
        ReviewListView.as_view(),
        name="review_list",
    ),
    path(
        "cabins/<int:cabin_id>/review/add/",
        ReviewCreateView.as_view(),
        name="add_review",
    ),
    path(
        "review/<int:pk>/edit/", ReviewEditView.as_view(), name="review_edit"
    ),
    path(
        "cabins/review/<int:pk>/delete/",
        ReviewDeleteView.as_view(),
        name="review_delete",
    ),
]
