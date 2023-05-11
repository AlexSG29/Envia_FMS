from django.shortcuts import render
from mantenimientos.models import Mantenimiento

#Para generar iformes
from django.http import HttpResponse
from django.views import View
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import io
import datetime


#Informes dashboard layout
def Informes(request):
    return render(request, 'informes/informes.html')


#Descargar Informe mantenimmientos Activos
class InformeMantenimientosActivos(View):
    def get(self, request):
        # Obtener todos los mantenimientos activos
        mantenimientos_activos = Mantenimiento.objects.filter(estado=True)

        # Crear el objeto PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="informe_mttos_activos.pdf"'

        # Generar el contenido del informe PDF
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)

       # Estilos del informe
        estilo_titulo = "Helvetica-Bold"
        estilo_fecha = "Helvetica"
        tamaño_titulo = 16
        tamaño_fecha = 9
        margen_izquierdo = 50
        margen_superior = 750
        dist_titulo_fecha = 35 #interlineado encabezado
        interlineado = 20

        # Encabezado del informe
        p.setFont(estilo_fecha, tamaño_fecha)
        fecha = f"Generado el: {datetime.datetime.now().strftime('%d de %B de %Y, %H:%M')}"
        fecha_width = p.stringWidth(fecha, estilo_fecha, tamaño_fecha)
        fecha_x = p._pagesize[0] - margen_izquierdo - fecha_width
        p.drawString(fecha_x, margen_superior, fecha)

        p.setFont(estilo_titulo, tamaño_titulo)
        titulo = "Informe de Mantenimientos Activos"
        titulo_width = p.stringWidth(titulo, estilo_titulo, tamaño_titulo)
        titulo_x = (p._pagesize[0] - titulo_width) / 2
        p.drawString(titulo_x, margen_superior - dist_titulo_fecha, titulo)

        # Agregar encabezados de tabla
        y = margen_superior - 2*dist_titulo_fecha
        encabezados = ['Placa', 'Fecha', 'Tipo']
        for i, encabezado in enumerate(encabezados):
            p.drawString(margen_izquierdo + i*150, y, encabezado)
        y -= interlineado

        # Agregar la lista de mantenimientos activos
        for mantenimiento in mantenimientos_activos:
            p.line(margen_izquierdo, y + 10, margen_izquierdo + 400, y + 10)  # línea divisoria
            p.drawString(margen_izquierdo, y, str(mantenimiento.placa))
            p.drawString(margen_izquierdo + 150, y, str(mantenimiento.fecha))
            p.drawString(margen_izquierdo + 300, y, mantenimiento.get_tipo_display())
            y -= interlineado

        p.showPage()
        p.save()

        # Finalizar el objeto PDF y devolver la respuesta
        buffer.seek(0)
        response.write(buffer.getvalue())
        buffer.close()
        return response
