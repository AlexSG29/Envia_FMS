from django import forms
from .models import Mantenimiento, RepuestoMantenimiento
from vehiculos.models import Vehiculo
from repuestos.models import Repuesto


class MantenimientoForm(forms.ModelForm):
    placa = forms.ModelChoiceField(queryset=Vehiculo.objects.all())

    class Meta:
        model = Mantenimiento
        fields = ['placa', 'tipo', 'proveedores', 'ot', 'os', 'fecha', 'fecha_preventivo', 'descripcion', 'estado']

    tipo = forms.ChoiceField(choices=Mantenimiento.TIPO_CHOICES, label='Tipo', 
                             widget=forms.Select(attrs={'class': 'form-control'}))

#Agregar repuesto a cada mantenimiento
class RepuestoMantenimientoForm(forms.ModelForm):
    repuesto = forms.ModelChoiceField(queryset=Repuesto.objects.all(), label='Repuesto')
    cantidad = forms.IntegerField(min_value=1, label='Cantidad')
    descripcion = forms.CharField(required=False, label='Descripción')

    class Meta:
        model = RepuestoMantenimiento
        fields = ('repuesto', 'cantidad', 'descripcion')
