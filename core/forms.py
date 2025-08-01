from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    calificacion = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=5,
        min_value=1,
        max_value=5
    )
    
    class Meta:
        model = Resena
        fields = ['calificacion', 'comentario', 'nombre']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre (opcional)'}),
        }