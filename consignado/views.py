from django.shortcuts import render

from rest_framework import viewsets
from .models import Consignataria, ConsultaMargemAthenas, Reserva
from .serializers import ConsignatariaSerializer, ConsultaMargemAthenasSerializer, ReservaSerializer

class ConsignatariaViewSet(viewsets.ModelViewSet):
    queryset = Consignataria.objects.all()
    serializer_class = ConsignatariaSerializer

class ConsultaMargemAthenasViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMargemAthenas.objects.all()
    serializer_class = ConsultaMargemAthenasSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

