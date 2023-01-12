from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

def index(request):
    infoSocios= loader.get_template("infoSocios.html")
    return HttpResponse(infoSocios.render())
