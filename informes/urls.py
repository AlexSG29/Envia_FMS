from django.urls import path
from . import views

urlpatterns = [
    path('', views.Informes, name='informes'), #Vista principal para descargar informes
    path('informe_activos/', views.InformeMantenimientosActivosView.as_view(), name='informe_activos') #Informe mttos activos
]