from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'), #Visualiza el perfil de usuario
    path('configuracion/', views.configuracion, name='configuracion'), #Visualiza la configuracion
    #path('registro/', views.registro, name='registro'),
    #path('registro-exitoso/', views.registro_existoso, name='registro_exitoso'),
]
