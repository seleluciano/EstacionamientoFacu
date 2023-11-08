from rest_framework import serializers
from .models import Sensor
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']

class  SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','estado']
