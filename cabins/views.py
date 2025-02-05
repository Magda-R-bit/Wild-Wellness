from django.shortcuts import render
from django.views.generic import ListView
from .models import Cabin


class CabinsListView(ListView):
    model = Cabin
    template_name = 'cabins/cabins_list.html'
    context_object_name = 'cabins'

