from django.db import models

class Consignataria(models.Model):
    nome = models.CharField(max_length=256)
    cpf_cnpj = models.CharField(max_length=14)

class ConsultaMargemAthenas(models.Model):
    margem_total = models.DecimalField(max_digits=10, decimal_places=2)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2)
    servidor = models.IntegerField()
    consignataria = models.IntegerField()

class Reserva(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    consulta = models.IntegerField()
    prazo_inicial = models.DateTimeField()
    prazo_final = models.DateTimeField()
    situacao = models.IntegerField()
    contrato = models.CharField(max_length=255)
