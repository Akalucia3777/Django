from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_list_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Camiones

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy
from .forms import CamionesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def inicio(request):
    home = loader.get_template('ventaCamiones/inicio.html')
    return HttpResponse(home.render())

def categoria(request,idCategoria):
    recetas= get_list_or_404(Camiones,categorias=idCategoria)
    
    ctx = {
        'recetas':recetas,
    }
    
    todas = loader.get_template('ventaCamiones/camiones_list.html')
    return HttpResponse(todas.render(ctx,request))

class CamionListView(ListView):
    model = Camiones
    
class CamionDetailView(DetailView):
    model = Camiones

class CamionCreateView(LoginRequiredMixin,CreateView):
    #para que si intenta modificar o borrar le mande al login si no esta logeado
    login_url = '/cuentas/login/'
    model = Camiones
    form_class=CamionesForm
    
    #un atajo mas rapido
    success_url = reverse_lazy('listado')

class CamionUpdateView(LoginRequiredMixin,UpdateView):
    #para que si intenta modificar o borrar le mande al login si no esta logeado
    login_url = '/cuentas/login/'
    
    model = Camiones
    
    form_class=CamionesForm
    template_name_suffix = '_update_form'
    
    success_url = reverse_lazy('listado')
    
class CamionDeleteView(DeleteView):
    model = Camiones
    
    success_url = reverse_lazy('listado')