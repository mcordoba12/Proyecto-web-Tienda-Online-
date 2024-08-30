from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from carro.views import limpiar_carro
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.urls import reverse


# Create your views here.

@login_required(login_url='/autentificacion/login/')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)#creamos un pedido
    carro = Carro(request) #creamos un carro
    lineas_pedido = list() #creamos una lista de lineas de pedido
    
    
    for key, value in carro.carro.items(): #recorremos el carro
        lineas_pedido.append(LineaPedido( #añadimos el producto al pedido
            
            producto_id = key,
            cantidad = value['cantidad'],
            user = request.user,
            pedido = pedido            
            
            )) 
    LineaPedido.objects.bulk_create(lineas_pedido) #guardamos las lineas de pedido
    
    
    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.user.username,
        email = request.user.email)
    
    messages.success(request, 'Pedido procesado correctamente')
    
    
    limpiar_carro(request)
    
    return redirect('Tienda') #redirigimos a la pagina de inicio
    
def enviar_mail(**kwargs):
    
    asunto = 'Gracias por tu pedido'
    mensaje = render_to_string("emails/pedido.html", {
            "pedido" : kwargs['pedido'], #pasamos el pedido,
            "lineas_pedido" : kwargs['lineas_pedido'], #pasamos las lineas de pedido
            "nombreusuario" : kwargs['nombreusuario']})#pasamos el nombre del usuario 
    
    mensaje_texto = strip_tags(mensaje) #pasamos el mensaje a texto plano y lo guardamos en mensaje_texto sin etiquetas html
    
    from_email = 'angela6309gonzalez@gmail.com' #correo de origen
    to= kwargs.get('email') #correo de destino
    
    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message = mensaje)
    

