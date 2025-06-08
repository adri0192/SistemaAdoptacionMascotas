from django import forms
from .models import SolicitudAdopcion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Cuéntanos por qué quieres adoptar a esta mascota...'})
        }
