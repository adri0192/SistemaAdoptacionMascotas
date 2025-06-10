from usuarios.models import Usuario
from mascotas.models import Mascota
from solicitudes.models import SolicitudAdopcion
from historiales.models import HistorialMedico
from django.utils import timezone

# Crear usuario admin
admin = Usuario.objects.create_user(
    username='admin1',
    email='admin1@example.com',
    password='admin123',
    rol='admin',
    is_staff=True,
    is_superuser=True
)
admin.save()

# Crear usuario adoptante
adoptante = Usuario.objects.create_user(
    username='adoptante1',
    email='adoptante1@example.com',
    password='adoptante123',
    rol='adoptante',
    is_staff=False,
    is_superuser=False
)
adoptante.save()

# Crear una mascota
mascota = Mascota.objects.create(
    nombre='Luna',
    especie='Perro',
    raza='Mestizo',
    edad=3,
    sexo='Hembra',
    descripcion='Muy amigable y juguetona',
    estado='Disponible'
)
mascota.save()

# Crear una solicitud de adopción
solicitud = SolicitudAdopcion.objects.create(
    usuario=adoptante,
    mascota=mascota,
    estado='Pendiente',
    fecha_solicitud=timezone.now()
)
solicitud.save()

# Crear un historial médico para la mascota
historial = HistorialMedico.objects.create(
    mascota=mascota,
    fecha=timezone.now(),
    descripcion='Vacunas al día, desparasitada'
)
historial.save()

print("Datos iniciales cargados correctamente.")
