from django.shortcuts import render
from .models import Producto
# Create your views here.

def tienda(request):
    
    productos = Producto.objects.all() #Obtenemos todos los productos de la base de datos
    
    
    return render(request, "tienda/tienda.html", {'productos': productos}) #Renderizamos la plantilla tienda.html para mostrarla en el navegador
