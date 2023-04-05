from django.shortcuts import render, redirect, get_object_or_404
from .models import Mantenimiento
from .forms import MantenimientoForm

#Para ver la lista de todos los mantenimientos
def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    context = {'mantenimientos': mantenimientos}
    return render(request, 'mantenimientos/lista_mantenimientos.html', context)

#Para agregar un nuevo mantenimiento
def agregar_mantenimiento(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    else:
        form = MantenimientoForm()
    return render(request, 'mantenimientos/agregar_mantenimiento.html', 
                  {'form': form})

#Para editar un mantenimiento
def editar_mantenimiento(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    else:
        form = MantenimientoForm(instance=mantenimiento)
    return render(request, 'mantenimientos/editar_mantenimiento.html', 
                  {'form': form, 
                   'mantenimiento': mantenimiento})

#Eliminar un mantenimiento
def eliminar_mantenimiento(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    if request.method == 'POST':
        mantenimiento.delete()
        return redirect('lista_mantenimientos')
    return redirect('lista_mantenimientos')