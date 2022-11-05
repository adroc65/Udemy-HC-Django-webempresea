# modelos para la administracion de los BLOGS
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField   # Para usar el editor enriquesido

# Se importan los usuarios registrados en el panel del Administrador de Django
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # Para que se muestren en español para la administración
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]     # Se ordenanpor fecha de creación a la inversa.

    def __str__(self):
        return self.name            # Se muestra el Nombre de cada registro


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')

    # Ojo al NOW abajo, le quito los parentesis asi cada vez que un nuevo modelo se llama
    # se genera la fecha actual si no se espesifica una.
    published = models.DateField(verbose_name='Fecha de Publicación', default=now)

    # Sube la imagen al directori /media/blog
    image = models.ImageField(verbose_name='Imagen', upload_to="blog", null=True, blank=True)

    # Se proceden a crear los campos para relacionar con otras Bases de Datos, el autor se
    # toma de los usuarios registrados en el panel del administrador.
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    # Para las categorias se desean poner varias, por tanto, se tiene una relación de
    # muchos a muchos, se hace como se muestra, importante el nombre "related_name"
    # este permite referenciar las diferentes categorias con un nombre mas simple
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # Para que se muestren en español para la administración
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]     # Se ordenanpor fecha de creación a la inversa.

    def __str__(self):
        return self.title           # Se muestra el Nombre de cada registro
