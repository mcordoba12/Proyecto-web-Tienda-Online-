from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin): #clase para personalizar el panel de administracion
    readonly_fields = ('created', 'updated') #campos solo de lectura
    

admin.site.register(Servicio, ServicioAdmin) #registra el modelo en el panel de administracion

