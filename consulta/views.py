from rest_framework import viewsets
from .models import ConsultaMargemAthenas
from .serializers import ConsultaMargemAthenasSerializer

class ConsultaMargemAthenasViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMargemAthenas.objects.all()
    serializer_class = ConsultaMargemAthenasSerializer
