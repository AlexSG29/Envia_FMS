from django.contrib import admin
from .models import Mantenimiento, RepuestoMantenimiento

class RepuestoMantenimientoInline(admin.TabularInline):
    model = RepuestoMantenimiento
    extra = 1

# Register your models here.
@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    inlines = [RepuestoMantenimientoInline]
    list_display = ('placa', 'tipo', 'ot', 'fecha', 'estado')
    list_filter = ('placa','tipo', 'fecha', 'estado')
    search_fields = ('placa__placa', 'descripcion', 'ot')

@admin.register(RepuestoMantenimiento)
class RepuestoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('mantenimiento', 'repuesto', 'cantidad', 'descripcion')
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "mantenimiento":
            kwargs["queryset"] = Mantenimiento.objects.filter(estado=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)