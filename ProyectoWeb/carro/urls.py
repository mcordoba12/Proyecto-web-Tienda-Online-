from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "carro" #nombre de la aplicacion para usar todas las urls

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"), #agregar producto al carrito
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"), #eliminar producto del carrito
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"), #restar producto del carrito
    path("limpiar/", views.limpiar_carro , name="limpiar"), #limpiar carrito
    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para cargar imagenes en el panel de administracion