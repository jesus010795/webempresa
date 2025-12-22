from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Category, Post


# Create your views here.
def list_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def category(request, category_id):
    data = Category.objects.get(pk=category_id).posts.all()
    return render(request, "blog/category.html", {"data": data})
