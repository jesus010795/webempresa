from django.db import models


# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["title"]
