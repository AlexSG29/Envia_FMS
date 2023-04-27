from django.urls import path
from . import views

urlpatterns = [
      path('lista_repuestos/', views.lista_repuestos, name='lista_repuestos'),#ver repuestos lista
      path('agregar_repuesto/', views.agregar_repuesto, name='agregar_repuesto'),#agregar repuesto
      path('editar_repuesto/<int:repuesto_id>/', views.editar_repuesto, name='editar_repuesto'),#editar el repuesto
      path('eliminar_repuesto/<int:repuesto_id>/', views.eliminar_repuesto, name='eliminar_repuesto'),#eliminar el repuesto

] 