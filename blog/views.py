from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Category, Post


# Create your views here.
def list_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def list_categories(request):
    categories = Category.objects.all()
    return render(request, "blog/categories.html", {"categories": categories})
