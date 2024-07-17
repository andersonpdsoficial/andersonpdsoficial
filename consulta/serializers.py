from rest_framework import serializers
from .models import ConsultaMargemAthenas

class ConsultaMargemAthenasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'
