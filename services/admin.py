from django.contrib import admin
from .models import Service


# Register your models here.
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "content", "image"]
    readonly_fields = ("created", "updated")


admin.site.register(Service, ServiceModelAdmin)
