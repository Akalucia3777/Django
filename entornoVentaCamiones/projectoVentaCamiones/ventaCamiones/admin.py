from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Camiones, Categorias

class CamionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('marca','modelo','author')
    ordering=('marca','author')
                                        #Se pone doble _ para que busque por nombre o username
    search_fields=('marca','modelo','author__username','categorias__nombre')
    date_hierarchy=('created')
    list_filter=('categorias__nombre','author__username')

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','descripcion')


admin.site.register(Camiones,CamionAdmin)
admin.site.register(Categorias,CategoriasAdmin)
