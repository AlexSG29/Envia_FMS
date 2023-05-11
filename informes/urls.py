from django.urls import path
from . import views

urlpatterns = [
    path('', views.Informes, name='informes') #Vista principal para descargar informes
]