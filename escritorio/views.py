from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, generics, status
from datetime import date
from django.db.models import Count
from escritorio.models import Advogado, Cliente, Processo, Agenda
from escritorio.serializers import AdvogadoSerializer, ClienteSerializer, ProcessoSerializer, AgendaSerializer

# Advogados
class AdvogadosViewSet(viewsets.ModelViewSet):
    queryset = Advogado.objects.all()
    serializer_class = AdvogadoSerializer

    @action(detail=False, methods=['get'])
    def populares(self, request):
        """Listar advogados com mais clientes"""
        advogados = Advogado.objects.annotate(num_clientes=Count('clientes')).order_by('-num_clientes')
        serializer = self.get_serializer(advogados, many=True)
        return Response(serializer.data)

# Clientes
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FiltrarClientesPorIdade(generics.ListAPIView):
    """Listar clientes por faixa de idade"""
    serializer_class = ClienteSerializer

    def get_queryset(self):
        idade_min = self.kwargs['idade_min']
        idade_max = self.kwargs['idade_max']
        hoje = date.today()
        clientes = Cliente.objects.filter(
            data_nascimento__lte=date(hoje.year - idade_min, hoje.month, hoje.day),
            data_nascimento__gte=date(hoje.year - idade_max, hoje.month, hoje.day)
        )
        return clientes

# Processos
class ProcessosViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer

    @action(detail=True, methods=['patch'])
    def atualizar_status(self, request, pk=None):
        """Atualizar o status de um processo"""
        processo = self.get_object()
        novo_status = request.data.get('status')
        if novo_status not in dict(Processo.STATUS_CHOICES).keys():
            return Response({"error": "Status inválido."}, status=status.HTTP_400_BAD_REQUEST)
        processo.status = novo_status
        processo.save()
        return Response({"message": "Status atualizado com sucesso!"}, status=status.HTTP_200_OK)

class BuscarProcessoPorNumero(generics.RetrieveAPIView):
    """Buscar processo pelo número"""
    serializer_class = ProcessoSerializer

    def get_queryset(self):
        numero = self.kwargs['numero']
        return Processo.objects.filter(numero=numero)

# Agenda
class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class AgendaPorAdvogadoData(generics.ListAPIView):
    """Listar compromissos de um advogado em uma data específica"""
    serializer_class = AgendaSerializer

    def get_queryset(self):
        advogado_id = self.kwargs['advogado_id']
        data = self.kwargs['data']
        return Agenda.objects.filter(advogado_id=advogado_id, data=data)
