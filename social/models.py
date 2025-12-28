from django.db import models


# Create your models here.
class Links(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(max_length=50, verbose_name="Red social")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Enlace")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]
