from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Usuario(AbstractUser):
    ROLES = [
        ('adoptante', 'Adoptante'),
        ('admin', 'Administrador'),
    ]
    
    telefono = models.CharField(max_length=15, blank=True, verbose_name="Teléfono")
    direccion = models.TextField(blank=True, verbose_name="Dirección")
    rol = models.CharField(max_length=10, choices=ROLES, default='adoptante', verbose_name="Rol")
    fecha_registro = models.DateTimeField(default=timezone.now, verbose_name="Fecha de registro")
    
    def has_module_perms(self, app_label):
        """Solo los admins pueden acceder al panel de Django"""
        return self.is_active and self.rol == 'admin'

    def has_perm(self, perm, obj=None):
        """Solo los admins tienen permisos en el panel de Django"""
        return self.is_active and self.rol == 'admin'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

