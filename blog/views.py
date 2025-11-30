from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from blog.models import Post


# Create your views here.
def list_posts(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})
