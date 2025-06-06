from django.db import models
from django.utils import timezone

# Create your models here.
 
class Mascota(models.Model):
    ESPECIES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('otro', 'Otro'),
    ]
    
    SEXO = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]
    
    ESTADO = [
        ('Disponible', 'Disponible para adopción'),
        ('adoptado', 'Adoptado'),
        ('en_proceso', 'En proceso de adopción'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    especie = models.CharField(max_length=15, choices=ESPECIES, verbose_name="Especie")
    raza = models.CharField(max_length=70, verbose_name="Raza")
    edad = models.PositiveIntegerField(help_text="Edad en años", verbose_name="Edad")
    sexo = models.CharField(max_length=10, choices=SEXO, verbose_name="Sexo")
    estado_adopcion = models.CharField(
        max_length= 15,
        choices=ESTADO,
        default="disponible",
        verbose_name= "Estado de adopción"
    )
    fecha_ingreso = models.DateTimeField(default=timezone.now, verbose_name="Fecha de ingreso")
    adoptante = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='mascotas_adoptadas',
        verbose_name='Adoptante'
    )

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class Meta:
    verbose_name = "Mascota"
    verbose_name_plural = "Mascotas"
    ordering = ['-fecha_ingreso']