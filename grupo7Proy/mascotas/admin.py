from django.contrib import admin
from .models import Mascota

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'edad', 'sexo', 'estado_adopcion', 'adoptante', 'fecha_ingreso')
    list_filter = ('especie', 'estado_adopcion', 'sexo', 'fecha_ingreso')
    search_fields = ('nombre', 'raza')
    readonly_fields = ('fecha_ingreso',)

# Registra el modelo Mascota con la clase MascotaAdmin
admin.site.register(Mascota, MascotaAdmin)