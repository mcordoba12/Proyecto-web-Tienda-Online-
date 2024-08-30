from django.urls import path
from .views import VRegistro, cerrar_sesion, login
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', VRegistro.as_view(), name="autentificacion"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('login/', login, name="login")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para cargar imagenes en el panel de administracion