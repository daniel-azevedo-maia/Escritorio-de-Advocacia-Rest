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
    email = models.EmailField(default='')
    telefone = models.CharField(max_length=15, default='')

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(default='')
    telefone = models.CharField(max_length=15, default='')
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=250)

    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return self.nome

class Processo(models.Model):
    STATUS_CHOICES = (
        ('AB', 'Aberto'),
        ('EM', 'Em andamento'),
        ('FI', 'Finalizado'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='processos')
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE, related_name='processos')
    numero = models.CharField(max_length=30, unique=True)
    descricao = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def __str__(self):
        return f"Processo {self.numero} - {self.status}"

class Agenda(models.Model):
    advogado = models.ForeignKey(Advogado, on_delete=models.CASCADE, related_name='agenda')
    data = models.DateField()
    horario = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"Agenda {self.data} - {self.horario} ({self.advogado.nome})"
