from django.db import models


class Sensor(models.Model):
    estado = models.BooleanField(default=False)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    DNI = models.IntegerField()
    telefono = models.IntegerField()