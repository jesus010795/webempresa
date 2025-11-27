from django.urls import path
from .views import ListServiceView

urlpatterns = [path("services/", ListServiceView.as_view(), name="services")]
