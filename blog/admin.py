from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ("created", "updated")


class PostModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "published",
        "author",
    ]
    readonly_fields = ("created", "updated")


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
