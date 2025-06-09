from django import forms
from .models import HistorialMedico
from mascotas.models import Mascota

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['mascota', 'descripcion', 'tratamiento']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'tratamiento': forms.Textarea(attrs={'rows': 3}),
        }

class FiltroHistorialForm(forms.Form):
    especie = forms.ChoiceField(
        choices=[('', 'Todas las especies')] + Mascota.ESPECIES,
        required=False
    )
    mascota = forms.ModelChoiceField(
        queryset=Mascota.objects.none(),
        required=False,
        empty_label="Seleccionar mascota"
    )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.rol == 'admin':
            self.fields['mascota'].queryset = Mascota.objects.all()
        elif user:
            self.fields['mascota'].queryset = user.mascotas_adoptadas.all()
