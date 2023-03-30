from django.urls import path
from . import views

urlpatterns = [
      path('lista/', views.proveedores, name='lista_proveedores'),
      path('agregar/', views.agregar_proveedor, name='agregar_proveedor'),
      path('eliminar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),
      path('editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
]