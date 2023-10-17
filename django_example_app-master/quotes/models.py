from django.db import models


class Sensor(models.Model):
    estado = models.BooleanField(default=False)
