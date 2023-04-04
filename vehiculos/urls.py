from django.urls import path
from . import views

urlpatterns = [
    path('agregar_vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('lista_vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('eliminar_vehiculo/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('editar_vehiculo/<int:vehiculo_id>/', views.editar_vehiculo, name='editar_vehiculo'),
]
