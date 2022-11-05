"""
CONTACT URL Configuration

"""

from django.urls import path
from . import views


urlpatterns = [
    # En este URL no se agrega en el path el "contact/" ya este se agrego en
    # el URLS.PY de WEBEMPRESA, sirve de las 2 formas, pero se hace asi mayor control.
    # Recordar modificar el archivo "..contact/views.py" para llegarle al template.
    path('', views.contact, name="contact"),
]
