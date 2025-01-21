from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escritorio.views import (
    AdvogadosViewSet, ClientesViewSet, ProcessosViewSet, AgendaViewSet,
    FiltrarClientesPorIdade, BuscarProcessoPorNumero, AgendaPorAdvogadoData
)

router = routers.DefaultRouter()
router.register('advogados', AdvogadosViewSet, basename='Advogados')
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('processos', ProcessosViewSet, basename='Processos')
router.register('agenda', AgendaViewSet, basename='Agenda')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('clientes/idade/<int:idade_min>/<int:idade_max>/', FiltrarClientesPorIdade.as_view()),
    path('processos/numero/<str:numero>/', BuscarProcessoPorNumero.as_view()),
    path('agenda/advogado/<int:advogado_id>/data/<str:data>/', AgendaPorAdvogadoData.as_view()),
]
