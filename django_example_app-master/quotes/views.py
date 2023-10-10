from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente,Sensor
from .serializers import SensorSerializer, ClienteSerializer

# Create your views here.

def main(request):
    return render(request, 'quotes/main.html')




class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

