from django.urls import path
from . import views

urlpatterns = [
      path('', views.cronograma_vista, name='cronograma_vista'),
      path('calendario/', views.calendar_view, name='cronograma'),
]
