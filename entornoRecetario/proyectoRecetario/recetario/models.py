from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=255)
    subNombre = models.CharField(max_length=255,null=True)
    imagen = models.CharField(max_length=255,null=True)
    ingredientes = models.TextField(null=True)
    receta = models.TextField(null=True)
    
    #si creas un objeto de la clase receta y le haces "print" te devuelve el return
    
    def __str__(self) -> str:
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.nombre
