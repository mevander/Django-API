from rest_framework import viewsets
from house.api import serializers
from house import models

class ImobiliariaViewSet(viewsets.ModelViewSet):
     serializer_class = serializers.ImobiliariaSerializer
     queryset = models.Imobiliaria.objects.all()

class ImovelViewSet(viewsets.ModelViewSet):
     serializer_class = serializers.ImovelSerializer
     queryset = models.Imovel.objects.all()