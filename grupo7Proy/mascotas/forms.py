from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'sexo', 'estado_adopcion']
        widgets = {
            'edad' : forms.NumberInput(attrs={'min':0})
        }