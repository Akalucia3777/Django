from django.contrib import admin

# Register your models here.

from .models import profesor,Grupos

class ProfesorAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('apellidos','nombre','asignatura')
    ordering=('apellidos','nombre')
    search_fields=('nombre','tipo')
    date_hierarchy=('created')
    

class GruposAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('curso','letra','numAlumnos')
    
admin.site.register(profesor,ProfesorAdmin)

admin.site.register(Grupos,GruposAdmin)


