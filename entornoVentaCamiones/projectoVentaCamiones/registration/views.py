from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

class RegistroView(CreateView):
    form_class = UserCreationForm
    
    success_url = reverse_lazy('login')
    
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login')+'?registrado'
    
    
    def get_form(self, form_class=None):
        form = super(RegistroView,self).get_form()
        
        form.fields['username'].widget = form.TextInput(attrs={'style':'background-color:red'})
        form.fields['password1'].widget = form.PasswordInput(attrs={'style':'background-color:green'})
        
        return form