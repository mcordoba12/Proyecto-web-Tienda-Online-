from django import forms
from django.shortcuts import render
from django.views.generic import View
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages

from pedidos.models import User
# Create your views here.

class VRegistro(View):
    
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registro/registro.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            auth_login(request, usuario)  # Usa el alias 'auth_login' aquí
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, 'registro/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home') #redirigir al home

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password') #obtener los datos del formulario
            usuario = authenticate(username=nombre_usuario, password=contraseña) #autentificar al usuario
            if usuario is not None:
                auth_login(request, usuario)
                return redirect('Home')  # Asegúrate de que 'Home' esté definido en tus URLs
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Usuario no válido')

    form = AuthenticationForm() #crear un formulario de autentificacion
    return render(request, 'login/login.html', {'form': form})
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
