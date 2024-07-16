from rest_framework import serializers
from .models import Consignataria, ConsultaMargemAthenas, Reserva

class ConsignatariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = '__all__'

class ConsultaMargemAthenasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
