from django.urls import path
from . import views

urlpatterns = [
    path('lista_mantenimientos/', views.lista_mantenimientos, name='lista_mantenimientos'), #ver el total de los mantenimientos
    path('agregar_mantenimiento/', views.agregar_mantenimiento, name='agregar_mantenimiento'), #agregar nuevo mantenimiento
    path('editar_mantenimiento/<int:pk>/', views.editar_mantenimiento, name='editar_mantenimiento'), #editar mantenimiento
    path('eliminar_mantenimiento/<int:pk>/', views.eliminar_mantenimiento, name='eliminar_mantenimiento'), #eliminar mantenimiento
]
