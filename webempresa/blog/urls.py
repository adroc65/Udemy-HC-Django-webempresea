"""
APP = BLOGS - URL Configuration

"""

from django.urls import path
from . import views


urlpatterns = [
    # En este URL no se agrega en el path el "blogs/" ya este se agregó en
    # el URLS.PY de WEBEMPRESA, sirve de las 2 formas, pero se hace asi mayor control.
    # Recordar modificar el archivo "..blogs/views.py" para llegarle al template
    path('', views.blog, name="blog"),

    # Acceso a las diferentes categorias, lo que se escribe en el Browser
    # debe de quedar tal como se muestra, esto "<category_id>" es un parámetro
    # dinámico, solo puede ser una Cadena de caracteres, como se desea pasar un
    # número en este campo se debe de espesificar el "int:"
    # Con esto se agrega dinamismo a la URL
    path('category/<int:category_id>/', views.category, name="category"),
]
