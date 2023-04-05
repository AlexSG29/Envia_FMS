from django.db import models
from repuestos.models import Repuesto
from proveedores.models import Proveedor
from vehiculos.models import Vehiculo


class Mantenimiento(models.Model):
    TIPO_CHOICES = [
        ('C', 'Correctivo'),
        ('P', 'Preventivo'),
    ]
    placa = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    proveedores = models.ManyToManyField(Proveedor, blank=True)
    ot = models.CharField(max_length=20, blank=True)
    os = models.BooleanField(default=False)
    fecha = models.DateField()
    fecha_preventivo = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=400, blank=True)
    repuestos = models.ManyToManyField(Repuesto, through='RepuestoMantenimiento', blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Mantenimiento {self.tipo} en {self.placa} en {self.fecha}"

#Adjuntar repuestos a cada mantenimiento
class RepuestoMantenimiento(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.repuesto} x {self.cantidad} - {self.mantenimiento}"