from django.shortcuts import render
from django.http import JsonResponse
from mantenimientos.models import Mantenimiento
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
#from django.urls import reverse
#from django.db.models import Q

@login_required
def eventos_mantenimientos(request):
    mantenimientos = Mantenimiento.objects.filter(estado=True)
    eventos = []
    for mantenimiento in mantenimientos:
        eventos.append({
            'title': f"{mantenimiento.tipo} - {mantenimiento.placa}",
            'start': str(mantenimiento.fecha),
            'color': 'red',  # color para los mantenimientos con fecha
        })
        if mantenimiento.fecha_preventivo:
            eventos.append({
                'title': f"{mantenimiento.tipo} - {mantenimiento.placa}",
                'start': str(mantenimiento.fecha_preventivo),
                'color': 'green',  # color para los mantenimientos con fecha_preventivo
            })

    # Define una función personalizada para serializar objetos Vehiculo
    def serialize_vehiculo(obj):
        return {
            'id': obj.id,
            'placa': obj.placa,
        }

    return JsonResponse(eventos, safe=False, encoder=DjangoJSONEncoder, 
        json_dumps_params={'default': serialize_vehiculo})

@login_required
def cronograma(request):
    return render(request, 'cronograma/calendar.html')
