from rest_framework import serializers
from escritorio.models import Advogado, Cliente, Processo, Agenda

class AdvogadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advogado
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'
