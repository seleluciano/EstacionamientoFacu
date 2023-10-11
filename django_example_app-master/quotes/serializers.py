from rest_framework import serializers
from .models import Sensor, Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','DNI','telefono']

class  SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['numero','estado']

