from django.db import models

class Vehiculo(models.Model):
    TIPO_OPCIONES = [
        ('PT', 'PT'),
        ('MT', 'MT'),
        # Agrega aquí todos los tipos de vehículos que quieras incluir
    ]
    placa = models.CharField(max_length=7, unique=True)
    tipo = models.CharField(max_length=2, choices=TIPO_OPCIONES, default='PT')
    marca = models.CharField(max_length=50, default='Chevrolet')
    modelo = models.CharField(max_length=50, default='N300')
    anio = models.PositiveIntegerField(blank=True, null=True)
    regional = models.CharField(max_length=2, default='03')

    def __str__(self):
        return self.placa
