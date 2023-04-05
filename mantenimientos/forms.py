from django import forms
from .models import Mantenimiento

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
