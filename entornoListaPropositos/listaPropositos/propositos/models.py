from django.db import models

#se define un modelo
class Propositos(models.Model):
    prop = models.CharField(max_length=255)
    fecObj = models.DateField()
    conseg = models.BooleanField()
    fecConseg = models.DateField(null=True)
