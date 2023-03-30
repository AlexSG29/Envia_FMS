from django.shortcuts import render
from .models import Proveedor


def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', 
                  {'proveedores': proveedores})