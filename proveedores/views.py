from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib.auth.decorators import login_required

#Vista para agregar un nuevo proveedor
@login_required
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/agregar_proveedor.html', 
                  {'form': form})

#Vista para ver todos los proveedores
@login_required
def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista_proveedores.html', 
                  {'proveedores': proveedores})

#Para poder eliminar los proveedores.
@login_required
def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
    proveedor.delete()
    return redirect('lista_proveedores')

# Vista para editar un proveedor existente
@login_required
def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'proveedores/editar_proveedor.html', 
                  {'form': form, 'proveedor': proveedor})

# Vista para mensajear a whatsapp del proveedor
@login_required
def whatsapp(request, celular):
    url = f"https://wa.me/+57{celular}"
    return redirect(url) 
