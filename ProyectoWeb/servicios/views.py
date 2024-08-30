from django.shortcuts import render
from servicios.models import Servicio


# Create your views here.
def servicios(request):  
    
    servicios = Servicio.objects.all() #Obtenemos todos los servicios de la base de datos
    context = {'servicios': servicios} 
    return render(request, "servicios\servicios.html", context) #Renderizamos la plantilla servicios.html para mostrarla en el navegador
