from django import forms
from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
                                                            'minlength':'10',
                                                            'maxlength': '10'}))
    
    class Meta:
        model = Proveedor
        fields = ['nombre', 'celular', 'correo', 'tipo', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

""" class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__' """
