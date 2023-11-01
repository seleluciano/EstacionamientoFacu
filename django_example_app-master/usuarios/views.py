from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from quotes.models import Sensor
from quotes.serializers import SensorSerializer, ClienteSerializer
from django.shortcuts import render
from usuarios.forms import ClienteCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

def main(request):
    return render(request, 'vue_templates/main.html')  

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)
    
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        DNI = request.POST['DNI']
        password = request.POST['password']
        user = authenticate(request, DNI=DNI, password=password)
        if user is not None:
            login(request, user)
            token= Token.objects.get_or_create(user=user)  # Obtener o crear un token para el usuario
            return JsonResponse({'token': token.key})  # Devolver el token al cliente
    return JsonResponse({})

@csrf_exempt
def actualizar_estado(request):
    if request.method == 'GET':
        estado = request.GET.get('estado', None)
        sensor_id = request.GET.get('id', None)

        if estado is not None and sensor_id is not None:
            Sensor.objects.filter(id=sensor_id).update(estado=estado)
            return JsonResponse({'mensaje': 'Estado actualizado correctamente'})
        else:
            return JsonResponse({'mensaje': 'Parámetro de estado o ID de sensor no proporcionado'}, status=400)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = []
    permission_classes = []


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    authentication_classes = []
    permission_classes = []
