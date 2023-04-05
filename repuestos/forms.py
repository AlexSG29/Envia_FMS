from django import forms
from .models import Repuesto

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del repuesto',
        }
