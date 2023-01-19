from django.contrib import admin

# Register your models here.
from .models import Receta,Categoria  

admin.site.register(Receta)
admin.site.register(Categoria)
