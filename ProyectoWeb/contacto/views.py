from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto() #instanciamos el formulario
    
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST) #pasamos los datos recibidos por POST al formulario
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre") #obtenemos los datos del formulario
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage("Mensaje desde App Django", #asunto
                                 "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido), #cuerpo
                                 "",['angela6309gonzalez@gmail.com'], reply_to=[email]) #email origen
                                 
            try:
                email.send() #enviamos el email
                return redirect("/contacto/?valido") #redireccionamos a la pagina de contacto con el parametro valido
            except:
                return redirect("/contacto/?novalido")#redireccionamos a la pagina de contacto con el parametro novalido
    
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto}) #pasamos el formulario a la plantilla contacto