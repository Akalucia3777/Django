from django.contrib import admin

# Register your models here.
from .models import Empresas

class EmpresasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','tipo','personaContacto')
    ordering=('nombre','personaContacto')
    search_fields=('nombre','tipo')
    date_hierarchy=('created')
    
    
admin.site.register(Empresas)