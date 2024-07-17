from django.db import models
from consignataria.models import Consignataria
from servidor.models import Servidor

class ConsultaMargemAthenas(models.Model):
    margem_total = models.DecimalField(max_digits=10, decimal_places=2)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    consignataria = models.ForeignKey(Consignataria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.servidor.nome} - {self.consignataria.nome}"
