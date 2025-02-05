from django.urls import path
from .views import CabinsListView

urlpatterns = [
    path('', CabinsListView.as_view(), name='cabins_list')
]