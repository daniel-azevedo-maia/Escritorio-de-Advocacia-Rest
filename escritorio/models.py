from django.db import models

class Advogado(models.Model):
    ESPECIALIDADES = (
        ('DC', 'Direito Civil'),
        ('DP', 'Direito Previdenciário'),
        ('DT', 'Direito do Trabalho'),
        ('PE', 'Direito Penal'),
        ('DD', 'Direito Digital'),
        ('DA', 'Direito Administrativo'),
        ('DE', 'Direito Empresarial'),
        ('TR', 'Direito Tributário'),
        ('AG', 'Direito Agrário'),
        ('CO', 'Direito Constitucional')
    )

    nome = models.CharField(max_length=120)
    numero_oab = models.CharField(max_length=20)
    especialidade = models.CharField(choices=ESPECIALIDADES, max_length=2, blank=False, null=False)
    email = models.EmailField(default = '')
    telefone = models.CharField(max_length=100, default = '')

    def __str__(self):
        return self.nome


class Cliente(models.Model):

    nome = models.CharField(max_length=120)
    email = models.EmailField(default='')
    telefone = models.CharField(max_length=100, default='')
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=250)

    advogado = models.ForeignKey(Advogado, on_delete = models.CASCADE, related_name = 'clientes', null = False, blank = False)

    def __str__(self):
        return self.nome