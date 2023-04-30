from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #Para la autenticacion de usuarios
    #path('cuenta/', include('cuenta.urls')),# Para las demas vistas en la cuenta de usuario
    path('', include('dashboard.urls')), #Para el dashboard
    path('mantenimientos/', include('mantenimientos.urls')), #Para los mantenimientos
    path('proveedores/', include('proveedores.urls')), #Para los proveedores
    path('repuestos/', include('repuestos.urls')), #Para los repuestos.
    path('vehiculos/', include('vehiculos.urls')), #Para las placas
    path('cronograma/', include('cronograma.urls')), #Para el cronograma
]
