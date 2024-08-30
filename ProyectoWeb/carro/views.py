from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request) #creamos un objeto de la clase Carro 
    producto = Producto.objects.get(id=producto_id) #obtenemos el producto por su id
    carro.agregar(producto=producto) #agregamos el producto al carro
    return redirect("Tienda") #redirigimos a la pagina de la tienda

def eliminar_producto(request, producto_id):
    carro = Carro(request) #creamos un objeto de la clase Carro
    producto = Producto.objects.get(id=producto_id) #obtenemos el producto por su id
    carro.eliminar(producto=producto) #eliminamos el producto del carro
    return redirect("Tienda") #redirigimos a la pagina de la tienda

def restar_producto(request, producto_id):
    carro = Carro(request) #creamos un objeto de la clase Carro
    producto = Producto.objects.get(id=producto_id) #obtenemos el producto por su id
    carro.restar_producto(producto=producto) #restamos el producto del carro
    return redirect("Tienda") #redirigimos a la pagina de la tienda


def limpiar_carro(request):
    carro = Carro(request) #creamos un objeto de la clase Carro
    carro.limpiar_carro() #limpiamos el carro
    return redirect("Tienda") #redirigimos a la pagina de la tienda