from django import forms
from .models import HistorialMedico

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['fecha', 'descripcion', 'tratamiento']
