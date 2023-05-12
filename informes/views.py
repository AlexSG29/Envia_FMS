from django.shortcuts import render
from django.http import HttpResponse
from mantenimientos.models import Mantenimiento


#Informes dashboard layout
def Informes(request):
    return render(request, 'informes/informes.html')


#Descargar Informe mantenimmientos Activos


