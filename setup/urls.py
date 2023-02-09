from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escritorio.views import AdvogadosViewSet, ClientesViewSet, ListaClientesAdvogado

router = routers.DefaultRouter()
router.register('advogados', AdvogadosViewSet, basename='Advogados')
router.register('clientes', ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('advogado/<int:pk>/clientes/', ListaClientesAdvogado.as_view()),

]
