from django.shortcuts import render
from mantenimientos.models import Mantenimiento, RepuestoMantenimiento
from django.contrib.auth.decorators import login_required


#Mostrar el dashboard.
@login_required
def dashboard(request):
    mantenimientos = Mantenimiento.objects.filter(estado=True)
    ultimos_repuestos = RepuestoMantenimiento.objects.filter(eliminado=False).order_by('-id')[:13]
    context = {'mantenimientos': mantenimientos,
               'ultimos_repuestos': ultimos_repuestos}
    return render(request, 'dashboard/dashboard.html', context)

