from django.contrib import admin
from .models import Pages


# Register your models here.
class PagesModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Pages, PagesModelAdmin)
