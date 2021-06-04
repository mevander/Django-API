from django.db import models
from uuid import uuid4
# Create your models here.

class Imobiliaria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Imovel(models.Model):

    statusList = (
        (0, "Ativo"),
        (1, "Inativo"),
    )

    tipoList = (
        (0, "Apartamento"),
        (1, "Casa"),
    )

    finalidadeList = (
        (0, "Residencial"),
        (1, "Comercial"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, null=False)
    descricao = models.CharField(max_length=255, null=False)
    status = models.CharField(max_length=1, choices=statusList, null=False)
    caracteristicas = models.CharField(max_length=255, null=True)
    tipo = models.CharField(max_length=1, choices=tipoList, null=False)
    finalidade = models.CharField(max_length=1, choices=finalidadeList)
    imobiliaria = models.OneToOneField(Imobiliaria, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


