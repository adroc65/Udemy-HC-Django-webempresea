from tabnanny import verbose
from django.db import models


# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    # Para manejar el ICON de la red social
    font_awesome = models.CharField(verbose_name="Font-awesome", max_length=75, default="fa-")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # Para que se muestren en español para la administración
    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["name"]     # Se ordenanpor fecha de creación a la inversa.

    def __str__(self):
        return self.name          # Se muestra el Nombre de cada registro
