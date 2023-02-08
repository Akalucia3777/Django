from django import forms
from .models import Camiones

class CamionesForm (forms.ModelForm):
    class Meta:
        model = Camiones
        fields = ['marca','modelo','imagen','precio','descripcion','kilometros','author','categorias']
        widgets = {
            'marca':forms.TextInput(attrs={'placeholder':'Introduce la marca','class':'form-control','style':'margin-top:20px'}),
            'modelo':forms.TextInput(attrs={'placeholder':'Introduce el modelo','class':'form-control'}),
            'precio':forms.TextInput(attrs={'placeholder':'Introduce el precio','class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'placeholder':'Escribe una descripcion','class':'form-control'}),
            'kilometros':forms.TextInput(attrs={'placeholder':'Introduce los km','class':'form-control'}),
        }
        
        labels = {
            'marca':'',
            'modelo':'',
            'imagen':'',
            'precio':'',
            'descripcion':'',
            'kilometros':'',
        }