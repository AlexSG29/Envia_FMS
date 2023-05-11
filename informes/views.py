from django.shortcuts import render

#Informes dashboard
def Informes(request):
    return render(request, 'informes/informes.html')