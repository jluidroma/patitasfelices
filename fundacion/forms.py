# fundacion/forms.py
from django import forms
from .models import SolicitudAdopcion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['mascota', 'nombre_solicitante', 'email_solicitante', 'telefono_solicitante', 'direccion_solicitante', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }

