from django.db import models

class Servidor(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.IntegerField()
