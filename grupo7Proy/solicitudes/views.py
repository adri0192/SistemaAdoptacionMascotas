from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import SolicitudAdopcion
from .forms import SolicitudAdopcionForm
from mascotas.models import Mascota
from usuarios.views import es_admin

@login_required
def solicitar(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    
    if mascota.estado_adopcion != 'Disponible':
        messages.error(request, 'Esta mascota ya no está disponible para adopción.')
        return redirect('mascotas:detalle', mascota_id=mascota.id)
    
    # Verificar si ya existe una solicitud
    if SolicitudAdopcion.objects.filter(usuario=request.user, mascota=mascota).exists():
        messages.warning(request, 'Ya has enviado una solicitud para esta mascota.')
        return redirect('mascotas:detalle', mascota_id=mascota.id)
    
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.mascota = mascota
            solicitud.save()
            messages.success(request, 'Solicitud de adopción enviada correctamente.')
            return redirect('solicitudes:mis_solicitudes')
    else:
        form = SolicitudAdopcionForm()
    
    return render(request, 'solicitudes/solicitar.html', {
        'form': form,
        'mascota': mascota
    })

@login_required
def mis_solicitudes(request):
    solicitudes = SolicitudAdopcion.objects.filter(usuario=request.user)
    return render(request, 'solicitudes/mis_solicitudes.html', {'solicitudes': solicitudes})

@user_passes_test(es_admin)
def gestionar(request):
    solicitudes = SolicitudAdopcion.objects.all()
    return render(request, 'solicitudes/gestionar.html', {'solicitudes': solicitudes})

@user_passes_test(es_admin)
def procesar(request, solicitud_id, accion):
    solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)
    
    if accion == 'aprobar':
        solicitud.aprobar()
        messages.success(request, f'Solicitud aprobada. {solicitud.mascota.nombre} ha sido adoptado por {solicitud.usuario.get_full_name()}.')
    elif accion == 'rechazar':
        solicitud.estado = 'rechazada'
        solicitud.save()
        messages.info(request, 'Solicitud rechazada.')
    
    return redirect('solicitudes:gestionar')
