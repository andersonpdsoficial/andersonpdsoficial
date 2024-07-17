from rest_framework import viewsets
from .models import Consignataria
from .serializers import ConsignatariaSerializer

class ConsignatariaViewSet(viewsets.ModelViewSet):
    queryset = Consignataria.objects.all()
    serializer_class = ConsignatariaSerializer
