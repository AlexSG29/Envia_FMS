from django.db import models

class Proveedor(models.Model):
    TIPO_OPCIONES = [
        ('M', 'Mecánico'),
        ('E', 'Electricista'),
        ('S', 'Proveedor de servicios'),
    ]

    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True)
    tipo = models.CharField(max_length=1, choices=TIPO_OPCIONES, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
