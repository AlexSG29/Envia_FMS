from django import forms
from .models import Vehiculo

# forms.py
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        labels = {
            'placa': 'Placa',
            'tipo': 'Tipo',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'anio': 'Año',
            'regional': 'Regional',
        }
    tipo = forms.ChoiceField(choices=Vehiculo.TIPO_OPCIONES, label='Tipo', 
                             widget=forms.Select(attrs={'class': 'form-control'}))
