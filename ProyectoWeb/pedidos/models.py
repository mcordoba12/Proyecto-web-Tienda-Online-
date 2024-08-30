from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import Sum, F, FloatField

# Create your models here.

User = get_user_model()

class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']
    

    def __str__(self):
        return self.id
    
    @property 
    def total(self):
        return self.lineapedido_set.aggregate(
            total =Sum(F('cantidad') * F('producto__precio'), output_field=FloatField())
        )["total"] 


class LineaPedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = 'lineas_pedidos'
        verbose_name = 'Linea de Pedido'
        verbose_name_plural = 'Lineas de Pedidos'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'
