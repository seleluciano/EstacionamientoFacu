from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensor
from usuarios.models import Cliente
from .serializers import SensorSerializer, ClienteSerializer
from django.shortcuts import render, redirect
from usuarios.forms import ClienteCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    return render(request, 'quotes/main.html')

def register(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = ClienteCreationForm()

    return render(request, 'usuarios/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        DNI = request.POST['DNI']
        password = request.POST['password']
        user = authenticate(request, DNI=DNI, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirigir a la página Estacionamiento
    return render(request, 'usuarios/login.html')

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

