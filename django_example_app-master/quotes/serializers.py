from rest_framework import serializers
from .models import Sensor
from usuarios.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','DNI','telefono']

class  SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','estado']

