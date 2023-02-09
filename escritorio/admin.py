from django.contrib import admin
from escritorio.models import Advogado, Cliente

class Advogados(admin.ModelAdmin):
    list_display = ('id', 'nome', 'numero_oab')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'oab',)
    list_per_page = 20

admin.site.register(Advogado, Advogados)


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)