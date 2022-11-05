from django.shortcuts import render, get_object_or_404
from .models import Category, Post


# Create your views here.
def blog(request):
    # Se procede a leer todos los OBJETOS que tiene el modelo Post
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})


# Se define el acceso a cada categoria, se espera el "ID" para
# identificar cada categoria. Ver URLS.PY para que se vea como es
# el acceso a las diferentes paginas HTML de las categorias
def category(request, category_id):
    # Con el "GET" se optiene la categoria espesífica, ojo como se usa el
    # "get_object_or_404", para mostrar el mensaje de página no encontrada
    category = get_object_or_404(Category, id=category_id)

    # Solo se pasa la Categoria, sin embargo en la pagina se puede hacer
    # mensiones del POST, esto gracias a una propiedad de DJANGO
    return render(request, "blog/category.html", {'category': category})
