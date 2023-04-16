from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm


""" def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('placa')
    regionales = set(vehiculos.values_list('regional', flat=True))
    regional_filtro = request.GET.get('regional')
    
    if regional_filtro:
        vehiculos = vehiculos.filter(regional=regional_filtro)
    
    return render(request, 'vehiculos/lista_vehiculos.html', 
                  {'vehiculos': vehiculos,
                   'regionales': regionales}) """

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('placa')
    regionales = set(vehiculos.values_list('regional', flat=True))
    tipos = set(vehiculos.values_list('tipo', flat=True))
    
    regional_filtro = request.GET.get('regional')
    tipo_filtro = request.GET.get('tipo')
    
    if regional_filtro:
        vehiculos = vehiculos.filter(regional=regional_filtro)
    
    if tipo_filtro:
        vehiculos = vehiculos.filter(tipo=tipo_filtro)
    
    return render(request, 'vehiculos/lista_vehiculos.html', 
                  {'vehiculos': vehiculos,
                   'regionales': regionales,
                   'tipos': tipos})



def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/agregar_vehiculo.html', 
                  {'form': form})

def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculo.delete()
    return redirect('lista_vehiculos')


def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/editar_vehiculo.html', 
                  {'form': form, 'vehiculo': vehiculo})