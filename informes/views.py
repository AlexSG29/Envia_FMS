from django.shortcuts import render
from mantenimientos.models import Mantenimiento, RepuestoMantenimiento
from django.contrib.auth.decorators import login_required
from datetime import datetime

#Informes dashboard layout
@login_required
def Informes(request):
    return render(request, 'informes/informes.html')


# informes/views.py
from django.views import View
from django.http import HttpResponse
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


#Vista que representa los informes de Mantenimientos de manera general
@login_required
def InformeMantenimientosActivosView(request):
    # Obtener los mantenimientos activos
    mantenimientos = Mantenimiento.objects.filter(estado=True)
        
    # Ajustar los márgenes de la página manualmente
    pagesize = letter
    left_margin = 1 * inch  # Margen izquierdo en pulgadas
    right_margin = 1 * inch  # Margen derecho en pulgadas
    top_margin = 0.25 * inch  # Margen superior en pulgadas
    bottom_margin = 0.25 * inch  # Margen inferior en pulgadas

    # Creamos el PDF en memoria
    buffer = HttpResponse(content_type='application/pdf')
    buffer['Content-Disposition'] = f'inline; filename="mantenimientos_activos.pdf"'
    doc = SimpleDocTemplate(buffer, pagesize=pagesize, 
                                leftMargin=left_margin, rightMargin=right_margin,
                                topMargin=top_margin, bottomMargin=bottom_margin
                                )

    # Estilos para el informe
    styles = {
            'Title': ParagraphStyle(name='Title', fontSize=17, alignment=1, 
                                    fontName='Courier-Bold',
                                    ),
            'Subtitle': ParagraphStyle(name='Subtitle', fontSize=12, alignment=1),
            'Timestamp': ParagraphStyle(name='Timestamp', fontSize=10, textColor=colors.gray, 
                                        fontName='Courier',
                                        ),
            'BlockTitle': ParagraphStyle(name='BlockTitle', fontSize=14, 
                                           fontName='Courier-Bold',
                                           ),
            'BlockContent': ParagraphStyle(name='BlockContent', fontSize=14, 
                                           fontName='Courier',
                                           ),
        }
       
        # Título y fecha
    titulo = Paragraph(f"Informe de Mantenimientos Activos", styles['Title'])
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    timestamp = Paragraph(f"Generado el {fecha_actual}", styles['Timestamp'])

    # Creamos la tabla con los datos
    data = [['Placa', 'Tipo', 'OT', 'Fecha de inicio']]
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
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),#Agrega un espacio de relleno en la parte inferior de la primera fila de la tabla.
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),#Alinear las placas a la izquierda
            ('ALIGN', (1, 0), (1, -1), 'CENTER'), #Alinear el tipo en el centro
            ('ALIGN', (2, 0), (2, -1), 'CENTER'), #Alinear la OT en el centro
            ('ALIGN', (3, 0), (3, -1), 'RIGHT'), #Alinear la fecha en la derecha
            ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'), #Establece la fuente  para la primera fila de la tabla.
            ('FONTNAME', (0, 1), (-1, -1), 'Courier'), #Establece la fuente  para el resto de la tabla.
            ('FONTSIZE', (0, 0), (-1, 0), 15), #Establece el tamaño de fuente para la primera fila de la tabla.
            ('FONTSIZE', (0, 1), (-1, -1), 13),#Establece el tamaño de fuente para el resto de la tabla.
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor("#151414")),#Dibuja una linea debajo de los encabezados de la tabla
        ]))

        # Ajustar el ancho de las columnas de la tabla
    table._argW[1] = 1.2 * inch
    table._argW[0] = 1.2 * inch
    table._argW[2] = 1.2* inch
    table._argW[3] = 2.75 * inch

    # Crear los bloques de información para cada mantenimiento
    blocks = []
    for mantenimiento in mantenimientos:
            # Información del mantenimiento
            placa = Paragraph(f"<b>{str(mantenimiento.placa)}</b> - {mantenimiento.get_tipo_display().upper()} que inició el {mantenimiento.fecha.strftime('%d de %B del %Y')}", 
                              styles['BlockContent']
                              )
            descripcion = Paragraph(f" <font color='#4F5050'><b>Descripcion:</b></font> {mantenimiento.descripcion}", 
                                    styles['BlockContent']
                                    )
            proveedores = Paragraph(f"<font color='#4F5050'><b>Proveedores:</b></font> {', '.join([str(proveedor) for proveedor in mantenimiento.proveedores.all()])}", 
                                    styles['BlockContent']
                                    )

            # Obtener los repuestos asociados al mantenimiento
            repuestos = RepuestoMantenimiento.objects.filter(mantenimiento=mantenimiento)
            repuestos_info = []
            for repuesto_mantenimiento in repuestos:
                repuesto_info = f" ({repuesto_mantenimiento.cantidad}) {repuesto_mantenimiento.repuesto} // <i>{repuesto_mantenimiento.descripcion}</i>"
                repuestos_info.append(Paragraph(repuesto_info, styles['BlockContent']))


            # Crear el bloque de información
            block = [
                Spacer(1, 0.2 * inch),
                placa,
                Spacer(1, 0.2 * inch),
                descripcion,
                Spacer(1, 0.1 * inch),
                proveedores,
                Spacer(1, 0.2 * inch),
            ]
            block.extend(repuestos_info)  # Agregar la información de los repuestos al bloque
            blocks.append(block)

    # Añadir una línea después de cada bloque de información
    line_style = ParagraphStyle(name='Line', spaceAfter=0.1 * inch, borderWidth=0.2, borderColor='grey')
    for i in range(len(blocks)):
            block = blocks[i]
            block.append(Spacer(1, 0.1 * inch))
            if i < len(blocks) - 1:
                block.append(Paragraph("<u> </u>", line_style))



        # Añadimos todo al PDF
    elements = [timestamp, Spacer(1, 0.3 * inch), titulo, Spacer(1, 0.7 * inch), table, Spacer(1, 0.7 * inch)]
    for block in blocks:
            elements.extend(block)
    doc.build(elements)

        

    return buffer

@login_required
def InformeMantenimientosInactivosView(request):
    # Obtener los mantenimientos activos
    mantenimientos = Mantenimiento.objects.filter(estado=False)
        
    # Ajustar los márgenes de la página manualmente
    pagesize = letter
    left_margin = 1 * inch  # Margen izquierdo en pulgadas
    right_margin = 1 * inch  # Margen derecho en pulgadas
    top_margin = 0.25 * inch  # Margen superior en pulgadas
    bottom_margin = 0.25 * inch  # Margen inferior en pulgadas

    # Creamos el PDF en memoria
    buffer = HttpResponse(content_type='application/pdf')
    buffer['Content-Disposition'] = f'inline; filename="mantenimientos_inactivos.pdf"'
    doc = SimpleDocTemplate(buffer, pagesize=pagesize, 
                                leftMargin=left_margin, rightMargin=right_margin,
                                topMargin=top_margin, bottomMargin=bottom_margin
                                )

    # Estilos para el informe
    styles = {
            'Title': ParagraphStyle(name='Title', fontSize=17, alignment=1, 
                                    fontName='Courier-Bold',
                                    ),
            'Subtitle': ParagraphStyle(name='Subtitle', fontSize=12, alignment=1),
            'Timestamp': ParagraphStyle(name='Timestamp', fontSize=10, textColor=colors.gray, 
                                        fontName='Courier',
                                        ),
            'BlockTitle': ParagraphStyle(name='BlockTitle', fontSize=14, 
                                           fontName='Courier-Bold',
                                           ),
            'BlockContent': ParagraphStyle(name='BlockContent', fontSize=14, 
                                           fontName='Courier',
                                           ),
        }
       
        # Título y fecha
    titulo = Paragraph(f"Informe de Mantenimientos Inactivos", styles['Title'])
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    timestamp = Paragraph(f"Generado el {fecha_actual}", styles['Timestamp'])

    # Creamos la tabla con los datos
    data = [['Placa', 'Tipo', 'OT', 'Fecha de inicio']]
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
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),#Agrega un espacio de relleno en la parte inferior de la primera fila de la tabla.
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),#Alinear las placas a la izquierda
            ('ALIGN', (1, 0), (1, -1), 'CENTER'), #Alinear el tipo en el centro
            ('ALIGN', (2, 0), (2, -1), 'CENTER'), #Alinear la OT en el centro
            ('ALIGN', (3, 0), (3, -1), 'RIGHT'), #Alinear la fecha en la derecha
            ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'), #Establece la fuente  para la primera fila de la tabla.
            ('FONTNAME', (0, 1), (-1, -1), 'Courier'), #Establece la fuente  para el resto de la tabla.
            ('FONTSIZE', (0, 0), (-1, 0), 15), #Establece el tamaño de fuente para la primera fila de la tabla.
            ('FONTSIZE', (0, 1), (-1, -1), 13),#Establece el tamaño de fuente para el resto de la tabla.
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor("#151414")),#Dibuja una linea debajo de los encabezados de la tabla
        ]))

        # Ajustar el ancho de las columnas de la tabla
    table._argW[1] = 1.2 * inch
    table._argW[0] = 1.2 * inch
    table._argW[2] = 1.2* inch
    table._argW[3] = 2.75 * inch

    # Crear los bloques de información para cada mantenimiento
    blocks = []
    for mantenimiento in mantenimientos:
            # Información del mantenimiento
            placa = Paragraph(f"<b>{str(mantenimiento.placa)}</b> - {mantenimiento.get_tipo_display().upper()} que inició el {mantenimiento.fecha.strftime('%d de %B del %Y')}", 
                              styles['BlockContent']
                              )
            descripcion = Paragraph(f" <font color='#4F5050'><b>Descripcion:</b></font> {mantenimiento.descripcion}", 
                                    styles['BlockContent']
                                    )
            proveedores = Paragraph(f"<font color='#4F5050'><b>Proveedores:</b></font> {', '.join([str(proveedor) for proveedor in mantenimiento.proveedores.all()])}", 
                                    styles['BlockContent']
                                    )

            # Obtener los repuestos asociados al mantenimiento
            repuestos = RepuestoMantenimiento.objects.filter(mantenimiento=mantenimiento)
            repuestos_info = []
            for repuesto_mantenimiento in repuestos:
                repuesto_info = f" ({repuesto_mantenimiento.cantidad}) {repuesto_mantenimiento.repuesto} // <i>{repuesto_mantenimiento.descripcion}</i>"
                repuestos_info.append(Paragraph(repuesto_info, styles['BlockContent']))


            # Crear el bloque de información
            block = [
                Spacer(1, 0.2 * inch),
                placa,
                Spacer(1, 0.2 * inch),
                descripcion,
                Spacer(1, 0.1 * inch),
                proveedores,
                Spacer(1, 0.2 * inch),
            ]
            block.extend(repuestos_info)  # Agregar la información de los repuestos al bloque
            blocks.append(block)

    # Añadir una línea después de cada bloque de información
    line_style = ParagraphStyle(name='Line', spaceAfter=0.1 * inch, borderWidth=0.2, borderColor='grey')
    for i in range(len(blocks)):
            block = blocks[i]
            block.append(Spacer(1, 0.1 * inch))
            if i < len(blocks) - 1:
                block.append(Paragraph("<u> </u>", line_style))



        # Añadimos todo al PDF
    elements = [timestamp, Spacer(1, 0.3 * inch), titulo, Spacer(1, 0.7 * inch), table, Spacer(1, 0.7 * inch)]
    for block in blocks:
            elements.extend(block)
    doc.build(elements)


    return buffer
   