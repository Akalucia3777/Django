
from .models import Compras
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def compras(request):
    lc= Compras.objects.all()
    context = {
        'compras':lc,
    }
    plantilla = loader.get_template('compras.html')
    return HttpResponse(plantilla.render(context,request))

def nuevo(request):
    #Te recupera el campo nuevoElemento del form
    nP= request.GET['nuevoProducto']
    nC= request.GET['nuevaCantidad']
    nU= request.GET['nuevaUnidad']
    
    compra = Compras(producto=nP,cantidad=nC,unidad=nU,comprado=False)
    compra.save()
    
    return HttpResponseRedirect(reverse('compras'))

def comprado(request,identificador):
    
    cmpr = Compras.objects.get(id=identificador)
    cmpr.comprado = True
    cmpr.save()
    
    return HttpResponseRedirect(reverse('compras'))

def anadir(request,identificador):
    
    cmpr = Compras.objects.get(id=identificador)
    cmpr.comprado = False
    cmpr.save()
    
    return HttpResponseRedirect(reverse('compras'))