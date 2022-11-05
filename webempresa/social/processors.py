# Este archivo se usara para extender las Redes Sociales a todo el proyecto.
# Se debe de incluir la función en SETTINGS global, en el apartado
# TEMPLATES, 'context_processors'

from .models import Link


def ctx_dict(request):
    ctx = {}
    # Se envia todo el contexto
    ctx['links'] = Link.objects.all()
    return ctx
