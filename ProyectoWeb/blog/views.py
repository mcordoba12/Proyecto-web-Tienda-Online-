from django.shortcuts import render
from blog.models import Post, Categoria


# Create your views here.

def blog(request):
    
    post = Post.objects.all() #Obtenemos todos los post de la base de datos
    context= {'posts': post} #Creamos un diccionario con la variable post
    return render(request, "blog/blog.html", context) #Renderizamos la plantilla blog.html para mostrarla en el navegador


def categoria(request, categoria_id):
    
    categoria = Categoria.objects.get(id=categoria_id) #Obtenemos la categoria por su id
    post = Post.objects.filter(categorias=categoria) #Obtenemos los post que pertenecen a la categoria seleccionada
    return render(request, "blog/categoria.html", {'categoria': categoria, 'posts': post}) #Renderizamos la plantilla categoria.html para mostrarla en el navegador