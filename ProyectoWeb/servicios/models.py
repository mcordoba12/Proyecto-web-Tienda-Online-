from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')#subir imagen a la carpeta servicios
    created = models.DateTimeField(auto_now_add=True)#fecha automatica
    updated = models.DateTimeField(auto_now=True)
    
    class Meta: #clase interna para configurar la clase
            verbose_name = 'servicio' #nombre en singular
            verbose_name_plural = 'servicios' #nombre en plural
            
            def __str__(self): #metodo para mostrar el titulo en el panel de administracion
                return self.titulo #retorna el titulo
