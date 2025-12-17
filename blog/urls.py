from django.urls import path
from .views import list_posts, category

urlpatterns = [
    path("", list_posts, name="blog"),
    path("category/<int:category_id>", category, name="category"),
]
