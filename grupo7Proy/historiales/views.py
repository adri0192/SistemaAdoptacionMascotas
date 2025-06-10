from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse
from .models import HistorialMedico
from .forms import HistorialMedicoForm, FiltroHistorialForm
from mascotas.models import Mascota
from usuarios.views import es_admin

@login_required
def lista(request):
    form = FiltroHistorialForm(request.GET, user=request.user)
    historiales = HistorialMedico.objects.none()
    
    if request.user.rol == 'admin':
        historiales = HistorialMedico.objects.all()
    else:
        # Solo mostrar historiales de mascotas adoptadas por el usuario
        historiales = HistorialMedico.objects.filter(
            mascota__adoptante=request.user
        )
    
    # Aplicar filtros
    if form.is_valid():
        especie = form.cleaned_data.get('especie')
        mascota = form.cleaned_data.get('mascota')
        
        if especie:
            historiales = historiales.filter(mascota__especie=especie)
        if mascota:
            historiales = historiales.filter(mascota=mascota)
    
    return render(request, 'historiales/lista.html', {
        'form': form,
        'historiales': historiales
    })

@user_passes_test(es_admin)
def agregar(request):
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial médico agregado correctamente.')
            return redirect('historiales:lista')
    else:
        form = HistorialMedicoForm()
    return render(request, 'historiales/agregar.html', {'form': form})

def cargar_mascotas_por_especie(request):
    especie = request.GET.get('especie')
    user = request.user

    if user.rol == 'admin':
        mascotas = Mascota.objects.all()
    else:
        mascotas = user.mascotas_adoptadas.all()
    
    if especie:
        mascotas = mascotas.filter(especie=especie)
    
    mascotas_data = [{'id': m.id, 'nombre': m.nombre} for m in mascotas]
    return JsonResponse({'mascotas': mascotas_data})


