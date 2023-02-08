from django import forms
from .models import Camiones

class CamionesForm (forms.ModelForm):
    class Meta:
        model = Camiones
        fields = ['marca','modelo','imagen','precio','descripcion','kilometros','author','categorias']
        widgets = {
            'marca':forms.TextInput(attrs={'style':'background-color:red'}),
            'modelo':forms.TextInput(attrs={'style':'background-color:yellow','placeholder':'escribe el modelo'}),
            'precio':forms.TextInput(attrs={'style':'background-color:red'}),
            'descripcion':forms.Textarea(attrs={'class':'bot'}),
            'kilometros':forms.TextInput(attrs={'style':'background-color:red'}),
        }