from django.db import models


class Sensor(models.Model):
    ID = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    estado = models.BooleanField(default=False)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    DNI = models.EmailField(max_length=10)
    telefono = models.CharField(max_length=15)
