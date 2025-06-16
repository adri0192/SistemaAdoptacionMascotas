from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from usuarios.models import Usuario
from mascotas.models import Mascota
from historiales.models import HistorialMedico

class Command(BaseCommand):
    help = 'Crea datos iniciales para el sistema de adopción'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando creación de datos iniciales...'))
        
        # Crear usuario administrador
        admin_user, created = Usuario.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@adopcion.com',
                'first_name': 'Administrador',
                'last_name': 'Sistema',
                'rol': 'admin',
                'is_staff': True,
                'is_superuser': True,
                'password': make_password('admin123')
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Usuario administrador creado: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('✓ Usuario administrador ya existe'))

        # Crear usuario adoptante de ejemplo
        adoptante_user, created = Usuario.objects.get_or_create(
            username='juan_perez',
            defaults={
                'email': 'juan@email.com',
                'first_name': 'Juan',
                'last_name': 'Pérez',
                'telefono': '555-1234',
                'direccion': 'Calle Principal 123',
                'rol': 'adoptante',
                'password': make_password('password123')
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Usuario adoptante creado: juan_perez / password123'))
        else:
            self.stdout.write(self.style.WARNING('✓ Usuario adoptante ya existe'))


        for mascota_data in mascotas_data:
            mascota, created = Mascota.objects.get_or_create(
                nombre=mascota_data['nombre'],
                defaults=mascota_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Mascota creada: {mascota.nombre}'))
                
                # Agregar historial médico de ejemplo
                HistorialMedico.objects.create(
                    mascota=mascota,
                    descripcion=f"Revisión inicial de {mascota.nombre}. Mascota en buen estado general.",
                    tratamiento="Vacunación completa y desparasitación. Próxima revisión en 6 meses."
                )
                self.stdout.write(self.style.SUCCESS(f'✓ Historial médico creado para {mascota.nombre}'))
            else:
                self.stdout.write(self.style.WARNING(f'✓ Mascota {mascota.nombre} ya existe'))

        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('DATOS INICIALES CREADOS EXITOSAMENTE!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS('Puedes iniciar sesión con:'))
        self.stdout.write(self.style.SUCCESS('- Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('- Adoptante: juan_perez / password123'))
        self.stdout.write(self.style.SUCCESS('='*50))
