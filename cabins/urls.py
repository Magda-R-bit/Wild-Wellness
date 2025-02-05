from django.urls import path
from .views import CabinsListView, CabinDetail

urlpatterns = [
    path("", CabinsListView.as_view(), name="cabins_list"),
    path("<int:pk>/", CabinDetail.as_view(), name = "cabin_detail"),

]
