from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#Informes dashboard layout
@login_required
def Informes(request):
    return render(request, 'informes/informes.html')