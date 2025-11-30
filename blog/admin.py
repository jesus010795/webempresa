from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ("created", "updated")
    ordering = ("name",)


class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "author", "post_categories")
    readonly_fields = ("created", "updated")
    ordering = ("-published",)
    search_fields = ("title", "content")
    list_filter = ("author__username", "categories__name")

    # Logica pra mostrar las categorias de cada post
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])

    # Renombrando el metodo para que en el admin se muestre "Categorias"
    # La invocacion en la list_display conserva el nombre de la funcion
    post_categories.short_description = "Categorias"


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
