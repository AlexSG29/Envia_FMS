from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), #Para el dashboard
    path('proveedores/', include('proveedores.urls')), #para los proveedores
]
