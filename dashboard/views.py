from django.shortcuts import render

#Mostrar el dashboard.
def dashboard(request):
    return render(request, 'dashboard/layout.html')