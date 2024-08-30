from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta: #clase interna para configurar la clase
            verbose_name = 'categoria' #nombre en singular
            verbose_name_plural = 'categorias' #nombre en plural
            

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #cuando un usuario se elimina se elimina el post
    categorias= models.ManyToManyField(Categoria) #Una categoria puede tener varios post y un post puede tener varias categorias
    
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo
    
    
