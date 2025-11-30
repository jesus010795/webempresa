from django.urls import path
from .views import ListServiceView

urlpatterns = [path("", ListServiceView.as_view(), name="services")]
