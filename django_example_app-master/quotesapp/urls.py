from django.contrib import admin
from django.urls import path, include
from quotes.views import main, register, ClienteViewSet, SensorViewSet, actualizar_estado, login_user
from rest_framework.routers import DefaultRouter
from quotes import views
from EstacionamientoUTN.src import routers
import json

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'sensores', SensorViewSet)

with open('../EstacionamientoFacu/src/router.json', 'r') as file:
    routes = json.load(file)

vue_urlpatterns = [
    path(route['path'], getattr(views, route['name']), name=route['name'])
    for route in routes
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('actualizar_estado/', actualizar_estado, name='actualizar_estado'),
    path('register/', register, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('registro/', routers.inicio, name='vue_registro'),
    path('inicio/', routers.inicio, name='vue_inicio'),
    path('estacionamiento/', routers.estacionamiento, name='vue_estacionamiento')
]

# Agregar las rutas de Vue al urlpatterns
urlpatterns += vue_urlpatterns
