from pyexpat import model
from django.db import models
# Create your models here.
class Region(models.Model):
    lugar=models.CharField(max_length=200)

class Candidato(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    res_nombre = models.CharField(max_length=200)
    res_apellido = models.CharField(max_length=200)
    res_partido = models.CharField(max_length=200)
    res_DNI = models.CharField(max_length=200)

