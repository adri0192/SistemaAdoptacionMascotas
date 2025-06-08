from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Usuario
from mascotas.models import Mascota
#from solicitudes.models import SolicitudAdopcion

def es_admin(user):
    return user.is_authenticated and user.rol == 'admin'

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('mascotas:inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@user_passes_test(es_admin)
def panel_admin(request):
    stats = {
        'total_mascotas': Mascota.objects.count(),
        'mascotas_disponibles': Mascota.objects.filter(estado_adopcion='disponible').count(),
        'mascotas_adoptadas': Mascota.objects.filter(estado_adopcion='adoptado').count(),
        #'solicitudes_pendientes': SolicitudAdopcion.objects.filter(estado='pendiente').count(),
        'total_usuarios': Usuario.objects.count(),
    }
    return render(request, 'usuarios/panel_admin.html', {'stats': stats})
