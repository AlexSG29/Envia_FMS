from django.shortcuts import render
from mantenimientos.models import Mantenimiento

#Mostrar el dashboard.
def dashboard(request):
    mantenimientos = Mantenimiento.objects.filter(estado=True)
    context = {'mantenimientos': mantenimientos}
    return render(request, 'dashboard/dashboard.html', context)

