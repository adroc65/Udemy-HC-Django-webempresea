"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings     # Se usa para poder ver los archivos media en desarrollo

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths de services, aqui se incluye "services/", pero en el URL propio
    # de services no se pone para poder llegar a la pagina solo con: 127.0.0.1:8000/services/
    path('services/', include('services.urls')),
    # Lo mismo que "SERVICES" con la APP "BLOGS"
    path('blog/', include('blog.urls')),
    path('page/', include('pages.urls')),
    path('contact/', include('contact.urls')),

    # Paths del admin
    path('admin/', admin.site.urls),
]

# Rutina para poder ver archivos tipo media (imagenes) en desarrollo
if settings.DEBUG:      # Se entra a esta rutina solo si se esta en DEBUG, esto es Desarrollo
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
