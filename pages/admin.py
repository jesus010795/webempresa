from django.contrib import admin
from .models import Pages


# Register your models here.
class PagesModelAdmin(admin.ModelAdmin):
    list_display = ["title", "order"]
    readonly_fields = ("created", "updated")


admin.site.register(Pages, PagesModelAdmin)
