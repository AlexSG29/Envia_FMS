from django.urls import path
from . import views

urlpatterns = [
      path('lista/', views.proveedores, name='lista_proveedores'),
]