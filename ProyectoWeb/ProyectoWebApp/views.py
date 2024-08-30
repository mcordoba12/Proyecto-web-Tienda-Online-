from django.shortcuts import render, HttpResponse

from carro.carro import Carro

# Create your views here.

def home(request):   
    carro = Carro(request) #instanciamos la clase Carro dedes aqui porque 
    return render(request, "ProyectoWebApp/home.html") #Renderizamos la plantilla home.html para mostrarla en el navegador




