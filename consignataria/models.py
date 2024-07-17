from django.db import models

class Consignataria(models.Model):
    nome = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
