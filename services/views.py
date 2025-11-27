from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Service


# Create your views here.
# def services(request):
#     return render(request, "core/services.html")


class ListServiceView(ListView):
    model = Service
    context_object_name = "services"
