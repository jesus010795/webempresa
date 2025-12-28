from django.contrib import admin
from .models import Links


# Register your models here.
class LinksModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Links, LinksModelAdmin)
