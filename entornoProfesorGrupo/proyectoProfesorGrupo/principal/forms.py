from django import forms
from .models import profesor

class ProfesorForm (forms.ModelForm):
    class Meta:
        model = profesor
        fields = ['nombre','apellidos','telefono','correo','asignatura','author','grupos']
        widgets = {
            'nombre':forms.TextInput(attrs={'placeholder':'Introduce un Nombre'}),
            'apellidos':forms.TextInput(attrs={'placeholder':'Introduce los apellidos'}),
            'telefono':forms.TextInput(attrs={'placeholder':'Introduce el telefono'}),
            'correo':forms.Textarea(attrs={'placeholder':'Escribe un correo'}),
            'asignatura':forms.TextInput(attrs={'placeholder':'Introduce la asignatura'}),
        }
        
        labels = {
        }