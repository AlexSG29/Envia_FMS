from django.urls import path
from . import views

urlpatterns = [
    path('eventos_mantenimientos/', views.eventos_mantenimientos, name='eventos_mantenimientos'),
    path('', views.cronograma, name='cronograma'),#para visualizar el cronograma
]
