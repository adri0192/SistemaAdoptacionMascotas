from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import AdminSite
from .models import Usuario

class CustomAdminSite(AdminSite):
    def has_permission(self, request):
        """Solo usuarios con rol admin pueden acceder"""
        return request.user.is_active and getattr(request.user, 'rol', None) == 'admin'

# Reemplazar el sitio de admin por defecto
admin.site.__class__ = CustomAdminSite

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'fecha_registro')
    list_filter = ('rol', 'fecha_registro', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {
            'fields': ('telefono', 'direccion', 'rol', 'fecha_registro')
        }),
    )
    
    readonly_fields = ('fecha_registro',)
    
    def has_module_permission(self, request):
        """Solo admins pueden ver este módulo"""
        return request.user.is_authenticated and request.user.rol == 'admin'
