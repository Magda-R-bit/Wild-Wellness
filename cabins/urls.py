from django.urls import path
from .views import (CabinsListView, CabinDetail, ReviewListView, ReviewCreateAJAXView, ReviewEditAJAXView, ReviewDeleteAJAXView)  


urlpatterns = [
    path("", CabinsListView.as_view(), name="cabins_list"),
    path("<int:pk>/", CabinDetail.as_view(), name="cabin_detail"),
    # Reviews
    path("cabins/<int:cabin_id>/reviews/", ReviewListView.as_view(), name="review_list"),
    path("cabins/<int:cabin_id>/review/add/", ReviewCreateAJAXView.as_view(), name="add_review"),
    path("review/<int:pk>/edit/", ReviewEditAJAXView.as_view(), name="review_edit_ajax"),
    path("review/<int:pk>/delete/", ReviewDeleteAJAXView.as_view(), name="review_delete_ajax"),
    
]
