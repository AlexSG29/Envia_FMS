from django.urls import path
from . import views

urlpatterns = [
    path('', views.Informes, name='informes'), #Vista principal para descargar informes
    #path('informes/activos/', views.InformeMantenimientosActivosView, name='informe_activos'),
    #path('informes/inactivos/', views.InformeMantenimientosInactivosView, name='informe_no_activos'),
]