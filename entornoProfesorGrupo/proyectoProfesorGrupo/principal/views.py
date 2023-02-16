from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

from .forms import ProfesorForm
from .models import profesor


# Create your views here.

class ProfesoresListView(ListView):
    model = profesor
    
class ProfesoresCreateView(CreateView):
    model = profesor
    form_class=ProfesorForm
    
    #un atajo mas rapido
    success_url = reverse_lazy('listado')
    
class ProfesoresUpdateView(UpdateView):
    
    model = profesor
    
    form_class=ProfesorForm
    template_name_suffix = '_update_form'
    
    success_url = reverse_lazy('listado')
    
class ProfesoresDeleteView(DeleteView):
    model = profesor
    
    success_url = reverse_lazy('listado')
    
