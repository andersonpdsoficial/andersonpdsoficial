from rest_framework import serializers
from .models import Consignataria

class ConsignatariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = '__all__'
