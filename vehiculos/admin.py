from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'tipo', 'marca', 'modelo', 'anio', 'regional')
    list_filter = ('tipo','regional')
