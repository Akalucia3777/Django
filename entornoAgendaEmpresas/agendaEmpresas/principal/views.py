from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404
from django.template import loader



from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy
from .models import Empresas
# Create your views here.

class EmpresaListView(ListView):
    model = Empresas

class EmpresaDetailView(DetailView):
    model = Empresas
    
class EmpresaCreateView(CreateView):
    model = Empresas
    fields = ['nombre','tipo','direccion','telefono','personaContacto']
    
    #un atajo mas rapido
    success_url = reverse_lazy('listado')
    
    #esto se usa mucho por los que se crea un atajo de perezosos
    # def get_success_url(self):
    #     return reverse('listado')

class EmpresaUpdateView(UpdateView):
    model = Empresas
    
    fields = ['nombre','tipo','direccion','personaContacto']
    template_name_suffix = '_update_form'
    
    success_url = reverse_lazy('listado')
    
class EmpresaDeleteView(DeleteView):
    model = Empresas
    
    success_url = reverse_lazy('listado')

# def listado(request):
#     #modelo
#     empresas = get_list_or_404(Empresas)
#     #contexto
#     ctx={
#         'empresas':empresas,
#     }
#     #template
#     listadoHTML = loader.get_template('principal/listado.html')
#     #return template
#     return HttpResponse(listadoHTML.render(ctx,request))
