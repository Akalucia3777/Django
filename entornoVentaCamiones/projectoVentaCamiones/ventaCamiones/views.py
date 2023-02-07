from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_list_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Camiones

from django.views.generic.list import ListView

from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    home = loader.get_template('ventaCamiones/inicio.html')
    return HttpResponse(home.render())
