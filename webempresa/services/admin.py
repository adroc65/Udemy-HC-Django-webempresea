# Desde este archivo es que se permite a Django administrar el Modelo creado para esta App.
from django.contrib import admin

# Register your models here.
from .models import Service


# Register your models here.
# Para permitir ver los campos de Fecha de creación y de modificacion
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Service, ServiceAdmin)
