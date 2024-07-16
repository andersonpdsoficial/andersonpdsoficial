from django.shortcuts import render

from rest_framework import viewsets
from .models import Servidor
from .serializers import ServidorSerializer

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer
