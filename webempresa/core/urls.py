"""
CORE URL Configuration

"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('about/', views.about, name="about"),
]
