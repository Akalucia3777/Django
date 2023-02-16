from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Grupos(models.Model):
    curso  = models.CharField(max_length=100,verbose_name="curso")
    letra = models.TextField(max_length=10,verbose_name="letra")
    descripcion = models.TextField(null=True,verbose_name="descripcion")
    numAlumnos = models.IntegerField(verbose_name="Numero de Alumnos")
    ubicacion  = models.CharField(max_length=100,verbose_name="ubicacion")
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')    

    class Meta:
        verbose_name='grupo'
        verbose_name_plural="grupos"
        ordering=['-created']

    def __str__(self):
        nombre= self.curso +" "+self.letra
        return nombre
    
class profesor(models.Model):
    nombre = models.CharField(max_length=200,verbose_name="Nombre")
    apellidos  = models.CharField(max_length=200,verbose_name="Apellidos")
    telefono = models.CharField(max_length=20,verbose_name="Telefono")
    correo = models.EmailField(max_length=200,null=True,verbose_name="correo")
    asignatura = models.CharField(max_length=200,verbose_name="asignatura")
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación ')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificación')
    author = models.ForeignKey(User,verbose_name='autor',on_delete=models.CASCADE)
    grupos = models.ManyToManyField(Grupos,verbose_name="grupos")
    
    class Meta:
        verbose_name='profesor'
        verbose_name_plural="profesores"
        ordering=['-created']
        
    def __str__(self) :
        nombre= self.nombre +" "+self.apellidos
        return nombre
