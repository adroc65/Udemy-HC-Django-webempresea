"""
SERVICES URL Configuration

"""

from django.urls import path
from . import views


urlpatterns = [
    # En este URL no se agrega en el path el "services/" ya este se agrego en
    # el URLS.PY de WEBEMPRESA, sirve de las 2 formas, pero se hace asi mayor control.
    # Recordar modificar el archivo "..services/views.py" para llegarle al template.
    path('', views.services, name="services"),
]
