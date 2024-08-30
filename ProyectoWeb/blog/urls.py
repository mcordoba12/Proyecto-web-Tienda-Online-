from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para cargar imagenes en el panel de administracion