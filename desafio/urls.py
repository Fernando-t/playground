from django.urls import path 
from .views import una_vista, crear_dato, listado_usuarios

urlpatterns = [
    path('', una_vista, name='index'),
    path('usuarios/', listado_usuarios, name='listado_usuarios'),
    path('crear-dato/', crear_dato, name='crear_dato'),
    
]