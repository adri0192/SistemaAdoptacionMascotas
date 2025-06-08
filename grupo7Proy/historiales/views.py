from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascota, HistorialMedico
from .forms import HistorialMedicoForm

def historial_lista(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    historiales = mascota.historiales.all()
    return render(request, 'historial_lista.html', {'mascota': mascota, 'historiales': historiales})

def historial_nuevo(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST)
        if form.is_valid():
            historial = form.save(commit=False)
            historial.mascota = mascota
            historial.save()
            return redirect('historial_lista', mascota_id=mascota.id)
    else:
        form = HistorialMedicoForm()
    return render(request, 'historial_form.html', {'form': form, 'mascota': mascota})
