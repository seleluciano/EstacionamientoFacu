from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensor
from .serializers import SensorSerializer,UserSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.authtoken.models import Token  # Agregada importación para Token
from rest_framework.decorators import api_view
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def main(request):
    return render(request, 'vue_templates/main.html')  

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            # Obtener o crear un token para el usuario recién registrado
            user = form.instance
            token, _= Token.objects.get_or_create(user=user)
            return JsonResponse({'token': str(token)})  # Devolver el token al cliente
        else:
            print(form.errors)
            return JsonResponse({'errors': form.errors}, status=400)
    
@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        #import pdb;
        #pdb.set_trace()
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)  # Obtener o crear un token para el usuario
            return JsonResponse({'token': str(token)})  # Devolver el token al cliente
    return JsonResponse({'error': 'Credenciales inválidas'}, status=400)

@api_view(['POST'])
def actualizar_estado(request):
    # Obtener los datos del request
    estado = request.data.get('estado')
    sensor_id = request.data.get('id')
    if estado is not None and sensor_id is not None:
            # Intentar convertir sensor_id a entero (si es necesario)
            sensor_id = int(sensor_id)
            # Intentar obtener el sensor con el id proporcionado
            sensor = Sensor.objects.filter(id=sensor_id).first()
            if sensor is not None:
                # El sensor con el id proporcionado existe, actualizar el estado
                sensor.estado = estado
                sensor.save()
                return JsonResponse({'mensaje': 'Estado actualizado correctamente'})
            else:
                # El sensor con el id proporcionado no existe, crear uno nuevo
                nuevo_sensor = Sensor.objects.create(id=sensor_id, estado=estado)
                return JsonResponse({'mensaje': f'Nuevo sensor creado con ID {nuevo_sensor.id}'})
    else:
        return JsonResponse({'mensaje': 'Parámetro de estado o ID de sensor no proporcionado'}, status=400)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    authentication_classes = []
    permission_classes = []
