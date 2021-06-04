from rest_framework import serializers
from house import models

class ImobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imobiliaria
        fields = '__all__'

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imovel
        fields = '__all__'