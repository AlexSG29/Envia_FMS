from django.shortcuts import render
from mantenimientos.models import Mantenimiento, RepuestoMantenimiento


#Mostrar el dashboard.
def dashboard(request):
    mantenimientos = Mantenimiento.objects.filter(estado=True)
    ultimos_repuestos = RepuestoMantenimiento.objects.filter(eliminado=False).order_by('-id')[:10]
    context = {'mantenimientos': mantenimientos,
               'ultimos_repuestos': ultimos_repuestos}
    return render(request, 'dashboard/dashboard.html', context)

