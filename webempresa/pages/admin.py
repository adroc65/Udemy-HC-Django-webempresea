from django.contrib import admin


# Register your models here.
from .models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Mostrar los Campos de Orden y de Título
    list_display = ('title', 'order')


admin.site.register(Page, PageAdmin)
