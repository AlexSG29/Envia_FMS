from django.shortcuts import render

# Create your views here.
def cronograma_vista(request):
    return render(request, 'cronograma/calendar.html')

from vehiculos.models import Vehiculo

def calendar_view(request):
    vehiculos = Vehiculo.objects.all()
    context = {
        'vehiculos': vehiculos
    }
    return render(request, 'cronograma/calendario.html', context)
