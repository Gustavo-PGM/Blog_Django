from django import forms
from .models import Comentarios

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nome', 'comentario', 'email']