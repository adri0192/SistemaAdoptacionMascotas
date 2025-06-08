from django.db import models
from mascotas.models import Mascota



class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historiales')
    fecha = models.DateField()
    descripcion = models.TextField()
    tratamiento = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historial de {self.mascota.nombre} -Fecha: {self.fecha}"



