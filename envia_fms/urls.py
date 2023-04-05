from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), #Para el dashboard
    path('mantenimientos/', include('mantenimientos.urls')), #Para los mantenimientos
    path('proveedores/', include('proveedores.urls')), #Para los proveedores
    path('repuestos/', include('repuestos.urls')), #Para los repuestos.
    path('vehiculos/', include('vehiculos.urls')), #Para las placas
]
