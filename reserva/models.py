from django.db import models
from consulta.models import ConsultaMargemAthenas

class Reserva(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    consulta = models.ForeignKey(ConsultaMargemAthenas, on_delete=models.CASCADE)
    prazo_inicial = models.DateTimeField()
    prazo_final = models.DateTimeField()
    situacao = models.IntegerField()
    contrato = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.consulta} - {self.valor}"
