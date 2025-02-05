from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cabin


class CabinsListView(ListView):
    model = Cabin
    template_name = "cabins/cabins_list.html"
    context_object_name = "cabins"


class CabinDetail(DetailView):
    model = Cabin
    template_name = "cabins/cabin_detail.html"
    context_object_name = "cabin"
