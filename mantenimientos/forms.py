from django import forms
from .models import Mantenimiento



class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['placa', 'tipo', 'proveedores', 'ot', 'os', 'fecha', 'fecha_preventivo', 'descripcion', 'estado']
