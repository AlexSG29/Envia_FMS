from django import forms
from .models import Mantenimiento, RepuestoMantenimiento
from repuestos.models import Repuesto


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['placa', 'tipo', 'proveedores', 'ot', 'os', 'fecha', 'fecha_preventivo', 'descripcion', 'estado']

#Agregar repuesto a cada mantenimiento
class RepuestoMantenimientoForm(forms.ModelForm):
    repuesto = forms.ModelChoiceField(queryset=Repuesto.objects.all(), label='Repuesto')
    cantidad = forms.IntegerField(min_value=1, label='Cantidad')
    descripcion = forms.CharField(required=False, label='Descripción')

    class Meta:
        model = RepuestoMantenimiento
        fields = ('repuesto', 'cantidad', 'descripcion')
