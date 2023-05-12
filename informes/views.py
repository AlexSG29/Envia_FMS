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
from reportlab.platypus import Frame, SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from datetime import datetime

import locale
locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')

#Descargar Informe mantenimmientos Activos
class InformeMantenimientosActivosView(View):
    def get(self, request):
        # Establecer la configuración regional
        locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')
        
        # Ajustar los márgenes de la página manualmente
        pagesize = letter
        left_margin = 1 * inch  # Margen izquierdo en pulgadas
        right_margin = 1 * inch  # Margen derecho en pulgadas
        top_margin = 0.25 * inch  # Margen superior en pulgadas
        bottom_margin = 0.25 * inch  # Margen inferior en pulgadas

        # Creamos el PDF en memoria
        buffer = HttpResponse(content_type='application/pdf')
        buffer['Content-Disposition'] = 'inline; filename="mantenimientos_activos.pdf"'
        doc = SimpleDocTemplate(buffer, pagesize=pagesize, 
                                leftMargin=left_margin, rightMargin=right_margin,
                                topMargin=top_margin, bottomMargin=bottom_margin
                                )

        # Obtenemos los mantenimientos activos
        mantenimientos = Mantenimiento.objects.filter(estado=True)

        # Estilos para el informe
        styles = {
            'Title': ParagraphStyle(name='Title', fontSize=16, alignment=1, fontName='Courier-Bold'),
            'Subtitle': ParagraphStyle(name='Subtitle', fontSize=12, alignment=1),
            'Timestamp': ParagraphStyle(name='Timestamp', fontSize=10, textColor=colors.gray),
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
                mantenimiento.get_tipo_display().upper(),
                mantenimiento.ot,
                mantenimiento.fecha.strftime("%d de %B del %Y"),
            ]
            data.append(row)

        table = Table(data)
        table.setStyle(TableStyle([
            #('BACKGROUND', (0, 0), (-1, 0), colors.lightblue), # Establece el color de fondo gris para la primera fila de la tabla.
            #('BACKGROUND', (0, 1), (-1, -1), colors.beige),#Establece el color de fondo beige para las filas restantes de la tabla.
            #('TEXTCOLOR', (0, 0), (-1, 0), colors.black),#Esto afecta a la primera fila de la tabla.
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),#Agrega un espacio de relleno en la parte inferior de la primera fila de la tabla.
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),#Alinear las placas a la izquierda
            ('ALIGN', (1, 0), (1, -1), 'CENTER'), #Alinear el tipo en el centro
            ('ALIGN', (2, 0), (2, -1), 'CENTER'), #Alinear la OT en el centro
            ('ALIGN', (3, 0), (3, -1), 'RIGHT'), #Alinear la fecha en la derecha
            ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'), #Establece la fuente  para la primera fila de la tabla.
            ('FONTNAME', (0, 1), (-1, -1), 'Courier'), #Establece la fuente  para el resto de la tabla.
            ('FONTSIZE', (0, 0), (-1, 0), 14), #Establece el tamaño de fuente para la primera fila de la tabla.
            ('FONTSIZE', (0, 1), (-1, -1), 10),#Establece el tamaño de fuente para el resto de la tabla.
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor("#151414")),
            #('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#2B2B2B"))#Agrega una cuadrícula con un ancho de línea y un color negro a todas las celdas de la tabla.
        ]))

        # Ajustar el ancho de las columnas de la tabla
        table._argW[1] = 1.2 * inch
        table._argW[0] = 1.2 * inch
        table._argW[2] = 1.2* inch
        table._argW[3] = 3 * inch

        # Añadimos todo al PDF
        elements = [timestamp, Spacer(1, 0.3 * inch), titulo, Spacer(1, 0.7 * inch), table]
        doc.build(elements)

        return buffer

