from django.db import models

#se define un modelo
class Compras(models.Model):
    producto = models.CharField(max_length=255)
    cantidad = models.FloatField()
    unidad = models.CharField(max_length=255)
    comprado = models.BooleanField()
