from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    DNI = models.IntegerField()
    telefono = models.IntegerField()
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=100)