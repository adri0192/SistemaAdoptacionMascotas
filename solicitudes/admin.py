from django.contrib import admin
from .models import SolicitudAdopcion

@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mascota', 'fecha_solicitud', 'estado')
    list_filter = ('estado', 'fecha_solicitud')
    search_fields = ('usuario__username', 'mascota__nombre')
    readonly_fields = ('fecha_solicitud',)
