from django.db import models
from django.utils import timezone

class SolicitudAdopcion(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, verbose_name="Usuario")
    mascota = models.ForeignKey('mascotas.Mascota', on_delete=models.CASCADE, verbose_name="Mascota")
    fecha_solicitud = models.DateTimeField(default=timezone.now, verbose_name="Fecha de solicitud")
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente', verbose_name="Estado")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    
    def __str__(self):
        return f"Solicitud de {self.usuario.username} para {self.mascota.nombre}"
    
    def aprobar(self):
        """Aprueba la solicitud y actualiza el estado de la mascota"""
        self.estado = 'aprobada'
        self.save()
        
        # Actualizar mascota
        self.mascota.estado_adopcion = 'adoptado'
        self.mascota.adoptante = self.usuario
        self.mascota.save()
        
        # Rechazar todas las demás solicitudes para esta mascota
        SolicitudAdopcion.objects.filter(
            mascota=self.mascota
        ).exclude(id=self.id).update(estado='rechazada')
    
    class Meta:
        verbose_name = "Solicitud de Adopción"
        verbose_name_plural = "Solicitudes de Adopción"
        unique_together = ['usuario', 'mascota']
        ordering = ['-fecha_solicitud']
