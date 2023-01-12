from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Propositos
from django.template import loader
from django.urls import reverse
from datetime import datetime,timedelta
import datetime

# Create your views here.
def propositos(request):
    lP=Propositos.objects.all()
    fechaActual=datetime.datetime.now().date()
    context = {
        'propositos':lP,
        'fechaActual':fechaActual,
    }
    plantilla = loader.get_template('propositos.html')
    return HttpResponse(plantilla.render(context,request))

def nuevProp(request):
    propNu = request.GET['propnuevo']
    fechaNu= request.GET['fech']
    
    propositoNu = Propositos(prop=propNu,fecObj=fechaNu,conseg=False)
    propositoNu.save()
    
    return HttpResponseRedirect(reverse('propositos'))

def conseguido(request,identificador):
    prop = Propositos.objects.get(id=identificador)
    prop.fecConseg = datetime.datetime.now()
    prop.conseg = True
    prop.save()
    
    return HttpResponseRedirect(reverse('propositos'))

def anadir(request,identificador):
    prop = Propositos.objects.get(id=identificador)
    prop.fecConseg = None
    prop.conseg = False
    prop.save()
    
    return HttpResponseRedirect(reverse('propositos'))

def borrar(request,identificador):
    prop = Propositos.objects.get(id=identificador)
    prop.delete()
    
    return HttpResponseRedirect(reverse('propositos'))



def modificarNombre(request,identificador):
    lP=Propositos.objects.get(id=identificador)
    context = {
        'propositos':lP,
    }
    plantilla = loader.get_template('modificarNombre.html')
    return HttpResponse(plantilla.render(context,request))

def actualizar(request,identificador):
    prop = Propositos.objects.get(id=identificador)
    prop.prop =request.GET['propnuevo']
    prop.save()
    
    return HttpResponseRedirect(reverse('propositos'))

def modificarFech(request,identificador):
    lP=Propositos.objects.get(id=identificador)
    context = {
        'propositos':lP,
    }
    plantilla = loader.get_template('modificarFech.html')
    return HttpResponse(plantilla.render(context,request))

def retrasarFech(request,identificador):
    prop = Propositos.objects.get(id=identificador)
    dias =int(request.GET['numDias'])
    if dias > 0:
        prop.fecObj = prop.fecObj - (-1*(timedelta(days=dias)))
        prop.save()
    
    return HttpResponseRedirect(reverse('propositos'))