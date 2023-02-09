from rest_framework import viewsets, generics
from escritorio.models import Advogado, Cliente
from escritorio.serializers import AdvogadoSerializer, ClienteSerializer

class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os advogados"""
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ListaClientesAdvogado(generics.ListAPIView):
    """Listando os clientes de um advogado"""
    def get_queryset(self):
        queryset = Cliente.objects.filter(advogado_id = self.kwargs['pk'])
        return queryset
    serializer_class = ClienteSerializer

