from django.shortcuts import render, redirect, get_object_or_404
from .models import Mantenimiento, RepuestoMantenimiento
from .forms import MantenimientoForm
from django.forms import inlineformset_factory

#Para ver la lista de todos los mantenimientos
def lista_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.all()
    context = {'mantenimientos': mantenimientos}
    return render(request, 'mantenimientos/lista_mantenimientos.html', context)


#Agregar un nuevo mantenimiento
def agregar_mantenimiento(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            mantenimiento = form.save()
            print('Mantenimiento guardado')
            return redirect('lista_mantenimientos')
        else:
            print('Datos inválidos')
    else:
        form = MantenimientoForm()

    context = {
        'form': form,
    }
    print('Renderizando el formulario')
    return render(request, 'mantenimientos/agregar_mantenimiento.html', context)

#Editar el mantenimiento
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

# Ver los repuestos asociados a ese mantenimiento
def ver_repuestos(request, mantenimiento_id):
    mantenimiento = get_object_or_404(Mantenimiento, pk=mantenimiento_id)
    repuestos_mantenimiento = mantenimiento.repuestomantenimiento_set.all()
    context = {
        'mantenimiento': mantenimiento,
        'repuestos': repuestos_mantenimiento,
    }
    return render(request, 'mantenimientos/ver_repuestos.html', context)
