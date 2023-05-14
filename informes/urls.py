from django.urls import path
from . import views

urlpatterns = [
    path('', views.Informes, name='informes'), #Vista principal para descargar informes
    path('informes/activos/', views.InformeMantenimientosActivosView.as_view(), name='informe_activos'),
    path('informes/noactivos/', views.InformeMantenimientosInactivosView.as_view(), name='informe_no_activos'),
]