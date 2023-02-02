from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Receta, Categorias

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','subnombre','author')
    ordering=('nombre','author')
                                        #Se pone doble _ para que busque por nombre o username
    search_fields=('nombre','subnombre','author__username','categorias__nombre')
    date_hierarchy=('created')
    list_filter=('categorias__nombre','author__username')

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','descripcion')


admin.site.register(Receta,RecetaAdmin)
admin.site.register(Categorias,CategoriasAdmin)