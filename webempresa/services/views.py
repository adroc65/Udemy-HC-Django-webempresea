from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    # Se procede a leer todos los OBJETOS que tiene el modelo de Proyecto
    services = Service.objects.all()
    # Se inyecta la lista de proyectos a la vista
    return render(request, "services/services.html", {'services': services})
