from django.contrib import admin
from django.urls import path, include
from quotes.views import main, register, ClienteViewSet, SensorViewSet, actualizar_estado, login_user
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'sensores', SensorViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('actualizar_estado/', actualizar_estado, name='actualizar_estado'),
    path('register/', register, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]