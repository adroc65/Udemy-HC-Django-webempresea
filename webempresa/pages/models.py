from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField   # Para usar el editor enriquesido


# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)

    # Se cambia la definición de "content", para usar el editor de texto.
    # Hay que hacer un "makemigrations" y "migrate", para que tome efecto
    # content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')

    # Campo para ordenar la forma de ver los registros.
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # Para que se muestren en español para la administración
    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        # Se usa de primero el campo "order"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title          # Se muestra el Nombre de cada registro
