from django.shortcuts import render
from mantenimientos.models import Mantenimiento

#Informes dashboard layout
def Informes(request):
    return render(request, 'informes/informes.html')


# informes/views.py
from django.views import View
from django.http import HttpResponse
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from datetime import datetime


#Descargar Informe mantenimmientos Activos
class InformeMantenimientosActivosView(View):
    def get(self, request):
        # Creamos el PDF en memoria
        buffer = HttpResponse(content_type='application/pdf')
        buffer['Content-Disposition'] = 'inline; filename="mantenimientos_activos.pdf"'
        doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

        # Obtenemos los mantenimientos activos
        mantenimientos = Mantenimiento.objects.filter(estado=True)

        # Estilos para el informe
        styles = {
            'Title': ParagraphStyle(name='Title', fontSize=16, alignment=1),
            'Subtitle': ParagraphStyle(name='Subtitle', fontSize=12, alignment=1),
            'Timestamp': ParagraphStyle(name='Timestamp', fontSize=10, textColor=colors.gray),
            'TableHeader': ParagraphStyle(name='TableHeader', fontSize=12, bold=True, textColor=colors.whitesmoke),
            'TableCell': ParagraphStyle(name='TableCell', fontSize=10, leading=12),
        }

        # Título y fecha
        titulo = Paragraph("Informe de Mantenimientos Activos", styles['Title'])
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        timestamp = Paragraph(f"Generado el {fecha_actual}", styles['Timestamp'])

        # Creamos la tabla con los datos
        data = [['Placa', 'Tipo', 'OT', 'Fecha']]
        for mantenimiento in mantenimientos:
            row = [
                str(mantenimiento.placa),
                mantenimiento.get_tipo_display(),
                mantenimiento.ot,
                mantenimiento.fecha.strftime("%d/%m/%Y"),
            ]
            data.append(row)

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue), # Establece el color de fondo gris para la primera fila de la tabla.
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),#Esto afecta a la primera fila de la tabla.
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'), #Alinea todo el contenido de la tabla al centro.
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), #Establece el nombre de la fuente como 'Helvetica-Bold' para la primera fila de la tabla.
            ('FONTSIZE', (0, 0), (-1, 0), 14), #Establece el tamaño de fuente para la primera fila de la tabla.
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),#Agrega un espacio de relleno en la parte inferior de la primera fila de la tabla.
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),#Establece el color de fondo beige para las filas restantes de la tabla.
            ('FONTSIZE', (0, 1), (-1, -1), 10),#Establece el tamaño de fuente para la primera el resto de la tabla.
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor("#151414")),
            #('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#2B2B2B"))#Agrega una cuadrícula con un ancho de línea y un color negro a todas las celdas de la tabla.
        ]))

        # Ajustar el ancho de las columnas de la tabla
        table._argW[0] = 1.5 * inch
        table._argW[1] = 2 * inch
        table._argW[2] = 1.5 * inch
        table._argW[3] = 1.5 * inch

        # Añadimos todo al PDF
        elements = [timestamp, Spacer(1, 0.25 * inch), titulo, Spacer(1, 0.25 * inch), table]
        doc.build(elements)

        return buffer

