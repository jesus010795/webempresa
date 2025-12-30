from django.urls import path
from .views import PageDetail

app_name = "pages"
urlpatterns = [path("<int:pk>/", PageDetail.as_view(), name="page_detail")]
