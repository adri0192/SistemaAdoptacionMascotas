from django import forms
from .models import HistorialMedico
from mascotas.models import Mascota

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['mascota', 'descripcion', 'tratamiento']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'tratamiento': forms.Textarea(attrs={'rows': 4}),
        }

class FiltroHistorialForm(forms.Form):
    ESPECIES = [('', 'Todas')] + Mascota.ESPECIES
    
    especie = forms.ChoiceField(
        choices=ESPECIES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mascota = forms.ModelChoiceField(
        queryset=Mascota.objects.none(),
        required=False,
        empty_label="Todas las mascotas",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Tanto admins como adoptantes pueden ver todas las mascotas
        self.fields['mascota'].queryset = Mascota.objects.all()
