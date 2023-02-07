from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_list_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Receta

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import RecetaForm

from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    home = loader.get_template('recetarioV3/inicio.html')
    return HttpResponse(home.render())

def receta(request):
    receta = Receta.objects.latest('created')
    ctx = {
        'receta':receta,
    }
    
    receta = loader.get_template('recetarioV3/receta.html')
    return HttpResponse(receta.render())

def desayunos(request):
    recetas = Receta.objects.filter(categorias__nombre='Desayuno')
    
    ctx = {
        'recetas':recetas,
    }
    todas = loader.get_template('recetarioV3/desayunos.html')
    return HttpResponse(todas.render(ctx,request))

def comidas(request):
    comidas = loader.get_template('recetarioV3/comidas.html')
    return HttpResponse(comidas.render())

def cenas(request):
    cenas = loader.get_template('recetarioV3/cenas.html')
    return HttpResponse(cenas.render())


def categoria(request,idCategoria):
    recetas= get_list_or_404(Receta,categorias=idCategoria)
    
    ctx = {
        'recetas':recetas,
    }
    
    todas = loader.get_template('recetarioV3/todas.html')
    return HttpResponse(todas.render(ctx,request))

class RecetaListView(ListView):
    model = Receta

class RecetaDetailView(DetailView):
    model = Receta
    
class RecetaCreateView(CreateView):
    model = Receta
    form_class=RecetaForm
    
    #un atajo mas rapido
    success_url = reverse_lazy('listado')
    
    #esto se usa mucho por los que se crea un atajo de perezosos
    # def get_success_url(self):
    #     return reverse('listado')

class RecetaUpdateView(UpdateView):
    model = Receta
    
    form_class=RecetaForm
    template_name_suffix = '_update_form'
    
    success_url = reverse_lazy('listado')
    
class RecetaDeleteView(DeleteView):
    model = Receta
    
    success_url = reverse_lazy('listado')