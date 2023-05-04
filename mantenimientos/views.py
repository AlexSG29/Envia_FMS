from django.shortcuts import render, redirect, get_object_or_404
from .models import Mantenimiento
from proveedores.models import Proveedor
from .forms import MantenimientoForm, RepuestoMantenimientoForm
from django.contrib.auth.decorators import login_required
#from vehiculos.models import Vehiculo


#Para ver la lista de todos los mantenimientos
@login_required
def lista_mantenimientos(request):
    estado = request.GET.get('estado', 'todos')
    tipo = request.GET.get('tipo', '')
    if estado == 'activos':
        mantenimientos = Mantenimiento.objects.filter(estado=True)
    elif estado == 'inactivos':
        mantenimientos = Mantenimiento.objects.filter(estado=False)
    else:
        mantenimientos = Mantenimiento.objects.all()

    if tipo:
        mantenimientos = mantenimientos.filter(tipo=tipo)

    context = {'mantenimientos': mantenimientos}
    return render(request, 'mantenimientos/lista_mantenimientos.html', context)



#Agregar un nuevo mantenimiento
@login_required
def agregar_mantenimiento(request):
    # Obtener los proveedores disponibles
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            mantenimiento = form.save()
            mantenimiento.proveedores.set(form.cleaned_data['proveedores'])
            mantenimiento.save()
            return redirect('lista_mantenimientos')
        else:
            print('Datos inválidos')
    else:
        form = MantenimientoForm()

    context = {
        'form': form,
        'proveedores': proveedores,
    }
    print('Renderizando el formulario')
    return render(request, 'mantenimientos/agregar_mantenimiento.html', context)


#Editar el mantenimiento
@login_required
def editar_mantenimiento(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    else:
        form = MantenimientoForm(instance=mantenimiento)
        form.fields['placa'].initial = mantenimiento.placa.pk
    return render(request, 'mantenimientos/editar_mantenimiento.html', 
                  {'form': form, 
                   'mantenimiento': mantenimiento,
                   'proveedores': proveedores})
""" def editar_mantenimiento(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        form = MantenimientoForm(request.POST, instance=mantenimiento)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenimientos')
    else:
        form = MantenimientoForm(instance=mantenimiento)
    return render(request, 'mantenimientos/editar_mantenimiento.html', 
                  {'form': form, 
                   'mantenimiento': mantenimiento,
                   'proveedores': proveedores}) """


#Eliminar un mantenimiento
@login_required
def eliminar_mantenimiento(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    if request.method == 'POST':
        mantenimiento.delete()
        return redirect('lista_mantenimientos')
    return redirect('lista_mantenimientos')

# Ver los repuestos asociados a ese mantenimiento
@login_required
def ver_repuestos(request, mantenimiento_id):
    mantenimiento = get_object_or_404(Mantenimiento, pk=mantenimiento_id)
    repuestos_mantenimiento = mantenimiento.repuestomantenimiento_set.all()
    context = {
        'mantenimiento': mantenimiento,
        'repuestos': repuestos_mantenimiento,
    }
    return render(request, 'mantenimientos/ver_repuestos.html', context)


# Agregar repuestos a ese mantenimiento
from django.contrib import messages

@login_required
def agregar_repuestos(request, mantenimiento_id):
    mantenimiento = get_object_or_404(Mantenimiento, pk=mantenimiento_id)

    if request.method == 'POST':
        form = RepuestoMantenimientoForm(request.POST)
        if form.is_valid():
            repuesto_mantenimiento = form.save(commit=False)
            repuesto = repuesto_mantenimiento.repuesto
            cantidad = repuesto_mantenimiento.cantidad
            descripcion = repuesto_mantenimiento.descripcion

            # Verificar si el repuesto ya está en la lista de repuestos asociados al mantenimiento
            repuestos_asociados = mantenimiento.repuestos.all()
            if repuestos_asociados.filter(mantenimientos__repuesto=repuesto).exists():
                messages.error(request, f'El repuesto "{repuesto}" ya está asociado a este mantenimiento.')
            else:
                # Agregar el nuevo repuesto al mantenimiento
                repuesto_mantenimiento.mantenimiento = mantenimiento
                repuesto_mantenimiento.save()
                messages.success(request, f'Se ha agregado el repuesto "{repuesto}" al mantenimiento "{mantenimiento}".')
                return redirect('agregar_repuestos', mantenimiento_id=mantenimiento_id)
    else:
        form = RepuestoMantenimientoForm()

    # Obtener los mensajes de la sesión
    messages_list = list(messages.get_messages(request))

    context = {
        'mantenimiento': mantenimiento,
        'form': form,
        'messages_list': messages_list,
    }
    return render(request, 'mantenimientos/agregar_repuestos.html', context)










