from django.shortcuts import render
from django.views.generic import DetailView

from .models import Pages


class PageDetail(DetailView):
    model = Pages
    context_object_name = "page"
