from django.shortcuts import render

# Create your views here.
def cronograma_vista(request):
    return render(request, 'cronograma/calendario.html')