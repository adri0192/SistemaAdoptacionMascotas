from django.contrib import admin
from .models import HistorialMedico

@admin.register(HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'fecha', 'descripcion')
    list_filter = ('fecha', 'mascota__especie')
    search_fields = ('mascota__nombre', 'descripcion')
    readonly_fields = ('fecha',)
