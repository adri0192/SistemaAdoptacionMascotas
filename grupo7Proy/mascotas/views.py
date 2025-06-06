from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Mascota
from .forms import MascotaForm
from usuarios.views import es_admin

# Create your views here.

def inicio(request):
    mascotas_disponibles = Mascota.objects.filter(estado_adopcion='disponible')
    return render(request, 'mascotas/inicio.html', {'mascotas' : mascotas_disponibles})

def detalle(request, mascota_id):
    mascota = get_list_or_404(Mascota, id=mascota_id)
    ya_solicito = False
    
    if request.user.is_authenticated:
        ya_solicito = mascota.solicitudadopcion_set.filter(usuario=request.user).exists()
    return render(request, 'mascotas/detalle.html',{
        'mascota' : mascota,
        'ya_solicito' : ya_solicito
    })
    
@user_passes_test(es_admin)
def gestionar(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/gestionar.html', {'mascotas' : mascotas})

@user_passes_test(es_admin)
def agregar(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota agregada correctamente')
            return redirect('mascotas:gestionar')
    else:
        form = MascotaForm()
    return render(request, 'mascotas/agregar.html', {'form' : form})

@user_passes_test(es_admin)
def editar(request, mascota_id):
    mascota = get_list_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mascota actualizada correctamente')
            return redirect('mascotas:gestionar')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascotas/editar.html', {'form' : form, 'mascota' : mascota})