from mantenimientos.models import Mantenimiento
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

#from django.template.loader import get_template


#Informes dashboard layout
def Informes(request):
    return render(request, 'informes/informes.html')



class InformeMantenimientosActivos(View):
    def get(self, request):
        # Obtener todos los mantenimientos activos
        mantenimientos_activos = Mantenimiento.objects.filter(estado=True)

        # Crear el objeto PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="informe_mttos_activos.pdf"'

        # Generar el contenido del informe PDF
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

        # Estilos del informe
        estilo_titulo = "Helvetica-Bold"
        estilo_texto = "Helvetica"
        tamaño_titulo = 16
        tamaño_texto = 12
        margen_izquierdo = 50
        margen_superior = 750
        interlineado = 20

        # Encabezado del informe
        p.setFont(estilo_titulo, tamaño_titulo)
        p.drawString(margen_izquierdo, margen_superior, "Informe de Mantenimientos Activos")
        p.setFont(estilo_texto, tamaño_texto)

        # Agregar la lista de mantenimientos activos
        y = margen_superior - interlineado
        for mantenimiento in mantenimientos_activos:
            texto = f"Placa: {mantenimiento.placa}, Fecha: {mantenimiento.fecha}, Tipo: {mantenimiento.get_tipo_display()}"
            p.drawString(margen_izquierdo, y, texto)
            y -= interlineado

        p.showPage()
        p.save()

        # Finalizar el objeto PDF y devolver la respuesta
        buffer.seek(0)
        response.write(buffer.getvalue())
        buffer.close()
        return response
