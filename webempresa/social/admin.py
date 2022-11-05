from django.contrib import admin

# Register your models here.
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'url')
    ordering = ('name', 'url')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('updated', 'key', 'name', 'font_awesome')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
