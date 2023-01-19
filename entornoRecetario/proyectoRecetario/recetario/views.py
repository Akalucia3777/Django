from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    home = loader.get_template('inicio.html')
    return HttpResponse(home.render())


def receta(request):
    receta = loader.get_template('receta.html')
    return HttpResponse(receta.render())

def desayuno(request):
    desayuno = loader.get_template('desayuno.html')
    return HttpResponse(desayuno.render())

def comidas(request):
    comidas = loader.get_template('comidas.html')
    return HttpResponse(comidas.render())

def cenas(request):
    cenas = loader.get_template('cenas.html')
    return HttpResponse(cenas.render())

def todas(request):
    todas = loader.get_template('todas.html')
    return HttpResponse(todas.render())