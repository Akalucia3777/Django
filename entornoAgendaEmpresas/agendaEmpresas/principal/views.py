from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404
from django.template import loader

from .models import Empresas
# Create your views here.

def listado(request):
    #modelo
    empresas = get_list_or_404(Empresas)
    #contexto
    ctx={
        'empresas':empresas,
    }
    #template
    listadoHTML = loader.get_template('principal/listado.html')
    #return template
    return HttpResponse(listadoHTML.render(ctx,request))
