# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Repuesto
from .forms import RepuestoForm

#Vista para poder todos los repuestos
def lista_repuestos(request):
    query = request.GET.get('q')
    if query:
        repuestos = Repuesto.objects.filter(nombre__icontains=query)
    else:
        repuestos = Repuesto.objects.all()
    return render(request, 'repuestos/lista_repuestos.html', {'repuestos': repuestos})



""" def lista_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'repuestos/lista_repuestos.html', 
                  {'repuestos': repuestos}) """

#Agregar nuevos repuestos
def agregar_repuesto(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_repuestos')
    else:
        form = RepuestoForm()
    return render(request, 'repuestos/agregar_repuesto.html', 
                  {'form': form})

#Editar los repuestos agregados
def editar_repuesto(request, repuesto_id):
    repuesto = get_object_or_404(Repuesto, id=repuesto_id)
    if request.method == 'POST':
        form = RepuestoForm(request.POST, instance=repuesto)
        if form.is_valid():
            form.save()
            return redirect('lista_repuestos')
    else:
        form = RepuestoForm(instance=repuesto)
    return render(request, 'repuestos/editar_repuesto.html', 
                  {'form': form, 'repuesto': repuesto})

#Eliminar los repuestos
def eliminar_repuesto(request, repuesto_id):
    repuesto = get_object_or_404(Repuesto, id=repuesto_id)
    if request.method == 'POST':
        repuesto.delete()
        return redirect('lista_repuestos')
    return render(request, 'repuestos/eliminar_repuesto.html', 
                  {'repuesto': repuesto})
