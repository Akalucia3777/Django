from .forms import UsuarioCrearFormConEmail
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


# Create your views here.

class RegistroView(CreateView):
    form_class = UsuarioCrearFormConEmail
    
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login');

    def get_success_url(self) -> str:
        return reverse_lazy('login')+'?registrado'
    
    
    def get_form(self, form_class=None):
        
        form = super(RegistroView,self).get_form()
        
        #modificamos los campos del formulario
        form.fields['username'].widget = forms.TextInput(attrs={'style':'background-color:lightgrey','placeholder':'Nombre'})
        form.fields['email'].widget = forms.EmailInput(attrs={'style':'background-color:lightgreen','placeholder':'email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'style':'background-color:green','placeholder':'contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'style':'background-color:green','placeholder':'contraseña'})
        
        return form