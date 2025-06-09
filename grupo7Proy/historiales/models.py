from django.db import models
from django.utils import timezone

class HistorialMedico(models.Model):
    mascota = models.ForeignKey(
        'mascotas.Mascota', 
        on_delete=models.CASCADE, 
        related_name='historial_medico',
        verbose_name="Mascota"
    )
    fecha = models.DateTimeField(default=timezone.now, verbose_name="Fecha")
    descripcion = models.TextField(verbose_name="Descripción")
    tratamiento = models.TextField(verbose_name="Tratamiento")
    
    def __str__(self):
        return f"Historial de {self.mascota.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
    
    class Meta:
        verbose_name = "Historial Médico"
        verbose_name_plural = "Historiales Médicos"
        ordering = ['-fecha']
