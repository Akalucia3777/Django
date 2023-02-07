from django import forms
from .models import Receta

class RecetaForm (forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre','subnombre','imagen','ingredientes','receta','categorias']
        widgets = {
            'nombre':forms.TextInput(attrs={'style':'background-color:red'}),
            'subnombre':forms.TextInput(attrs={'style':'background-color:yellow','placeholder':'escribe el subnombre'}),
            'ingredientes':forms.Textarea(attrs={'class':'bot'}),
        }
        labels = {
            'subnombre':'',
        }