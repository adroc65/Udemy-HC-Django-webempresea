from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField   # Para usar el editor enriquesido


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Sub Título')

    # Se cambia la definición de "content", para usar el editor de texto.
    # Hay que hacer un "makemigrations" y "migrate", para que tome efecto
    content = RichTextField(verbose_name='Contenido')

    # Sube la imagen al directori /media/services
    image = models.ImageField(verbose_name='Imagen', upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # Para que se muestren en español para la administración
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]             # Se ordenanpor fecha de creación a la inversa.

    def __str__(self):
        return self.title   # Se muestra el títilo de cada registro
