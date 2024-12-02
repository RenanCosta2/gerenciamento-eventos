from django.db import models

class Local(models.Model):
    nome = models.CharField(max_length=150)
    logradouro = models.CharField(max_length=255)
    numero = models.PositiveIntegerField(null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    capacidade = models.PositiveBigIntegerField()

    def __str__(self):
        numero = f", {self.numero}" if self.numero else ""
        return (
            f"{self.nome} - {self.logradouro}{numero}, "
            f"{self.bairro}, {self.cidade.name} - {self.estado.name}, "
            f"CEP: {self.cep}"
        )

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"
    
class Evento(models.Model):
    STATUS = [
        ("PLANEJADO", "Planejado"),
        ("CONFIRMADO", "Confirmado"),
        ("EM_ANDAMENTO", "Em Andamento"),
        ("FINALIZADO", "Finalizado"),
        ("CANCELADO", "Cancelado"),
    ]

    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    orcamento = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(choices=STATUS, default="PLANEJADO", max_length=12)
    dataInicio = models.DateTimeField()
    dataFim = models.DateTimeField()
    observacoes = models.TextField(null=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT)

    def __str__(self):
        return f"Evento {self.titulo}"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Custo(models.Model):
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - {self.valor}"
    
    class Meta:
        verbose_name = "Custo"
        verbose_name_plural = "Custos"
